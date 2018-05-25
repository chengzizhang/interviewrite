class node():
    def __init__(self,k=None,l=None,r=None):
        self.key=k
        self.left=l
        self.right=r
class btree():
    def __init__(self):
        self.root=None
    def create(self):


         a=input('enter a number')

         if a == 124:
              root=None
              return root
         else:

             root=node(k=a)
             root.left=create(root.left)
             root.right=create(root.right)
         return root
    def preorder(root):
         if root is None:
             return
         else:
             print(root.key)
             preorder(root.left)
             preorder(root.right)

    def inorder(root):
         if root is None:
             return
         else:
             inorder(root.left)
             print(root.key)
             inorder(root.right)

    def postorder(root):
         if root is None:
             return
         else:
             postorder(root.left)
             postorder(root.right)
             print(root.key)
root=None
root=create(root)
preorder(root)
inorder(root)
postorder(root)
