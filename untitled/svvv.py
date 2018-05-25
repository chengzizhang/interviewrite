import os
import numpy as np

from parrots import ssdata
from parrots.dnn import LearningSetting, FlowSpec, Session, AdamUpdater

from senseclass.base import ImageSet
from senseclass.frontend.simple import Callback, NetProgress, TrainNN
from senseclass.core.augmentation import *


class GAN(object):
    def __init__(self, module, flows, var_imgen):
        self.module = module
        self.flows = flows
        self.var_imgen = var_imgen

        # default session
        default_lr = 1e-4
        learning_setting = LearningSetting(lr=default_lr)
        updater = AdamUpdater(beta1=0.5)
        session = Session(module, learning_setting, updater)
        self.session = session

        # data flow for :
        #  - G: training G
        #  - D: training D
        #  - O: generating image using G
        gflow, dflow, oflow = flows

        cfg_train = {
            'devices': 'gpu(0)',
            'is_learn': True,
            'batch_size': module.max_bs
        }
        cfg_eval = {
            'devices': 'gpu(0)',
            'is_learn': False,
            'batch_size': module.max_bs
        }
        g_spec = FlowSpec(gflow, **cfg_train)
        d_spec = FlowSpec(dflow, **cfg_train)
        o_spec = FlowSpec(oflow, **cfg_eval)

        session.add_flow('G', g_spec)
        session.add_flow('D', d_spec)
        session.add_flow('O', o_spec)

        session.setup()

    def train(self, imgset, lr=1e-4, epoch=10, bs=256, callback=None):

        # the None callback do nothing, but compatible with code below
        if callback is None:
            callback = Callback()

        module = self.module
        flows = self.flows
        session = self.session

        session.csession._config(
            ssdata.SSElement.create({
                'learn': {
                    'lr': lr
                }
            }))
        session.init_param()

        if not isinstance(imgset, ImageSet):
            raise TypeError("GAN is only support training on ImageSet")

        aug_fun = compose(
            check_dim(ndim=4),
            to_float32(),
            standardize(mean=0, scale=255.),
            resize((module.imh, module.imw)),
            transpose(order=[2, 1, 3, 0]))

        # extract the structure parameter
        num_losses = module.num_losses
        dim_z = module.dim_z

        # ground-truth input for G and D repectively
        g_ones = np.ones([num_losses, bs], dtype=np.float32)
        d_ones = np.ones([num_losses, bs], dtype=np.float32)
        d_ones -= np.random.rand(*[num_losses, bs]).astype(np.float32) * 0.03
        d_zeros = np.random.rand(*[num_losses, bs]).astype(np.float32) * 0.03

        callback.setup()

        for ep in range(epoch):
            index = np.random.permutation(imgset.num_samples)
            for i in range(0, imgset.num_samples - bs, bs):
                e = i + bs
                # get real data
                Xs = imgset[index[i:e]]  #shape=(n,h,w,c)
                Xs = aug_fun(Xs)
                # get rand noise
                Zs = np.random.uniform(
                    0, 1, size=[dim_z, bs]).astype(np.float32)

                with session.flow('D') as flow:
                    flow.set_input('Z', Zs, set_spec=True)
                    flow.set_input('d_ones', d_ones, set_spec=True)
                    flow.set_input('d_zeros', d_zeros, set_spec=True)
                    flow.set_input('image_real', Xs, set_spec=True)
                    flow.forward()
                    flow.backward()
                    session.update_param()
                    if i == 0:
                        print 'iter: {}, update D, total loss is {}'.format(
                            ep, flow.total_loss / (num_losses + 10))

                with session.flow('G') as flow:
                    flow.set_input('Z', Zs, set_spec=True)
                    flow.set_input('g_ones', g_ones, set_spec=True)
                    flow.forward()
                    flow.backward()
                    session.update_param()
                    if i == 0:
                        print 'iter: {}, update G, total loss is {}'.format(
                            ep, flow.total_loss / (num_losses + 10))

    def generate(self, nimg=5):
        module = self.module
        flows = self.flows
        image_gen = self.var_imgen
        session = self.session
        dim_z = module.dim_z

        Zs = np.random.uniform(0, 1, size=[dim_z, nimg]).astype(np.float32)

        with session.flow('O') as flow:
            flow.set_input('Z', Zs, set_spec=True)
            flow.forward()
            generated_samples = image_gen.data.value()

        return generated_samples.transpose([3, 1, 0, 2])

    def save(self, path):
        self.session.dump_param(path)

    def load_param(self, path):
        if os.path.exists(path):
            self.session.load_param(str(path))
        else:
            raise IOError(
                "Parameter file {} does not exist. Load FAILED".format(path))


def dcgan_mnist():
    from .models.dcgan_mnist import get_module
    main, flows, image_gen = get_module()
    return GAN(main, flows, image_gen)


def dcgan(dim_z=100, base_hidden_channel=32, num_losses=10):
    from .models.dcgan import get_module
    main, flows, image_gen = get_module(dim_z, base_hidden_channel, num_losses)
    return GAN(main, flows, image_gen)


def gan(name, **kwargs):
    if name in gan_table.keys():
        return gan_table[name](**kwargs)
    else:
        raise ValueError("Unknown GAN network *{}*. ".format(
            name) + "Available GAN networks are {}. ".format(gan_table.keys()))


gan_table = {"DCGAN-MNIST": dcgan_mnist, "DCGAN": dcgan}
