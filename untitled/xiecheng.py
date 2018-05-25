import math

string = input()
str_list = list(string)
n = len(str_list)
str_list_single = list(set(str_list))
num_list = []
for i in str_list_single:
    num_list.append(str_list.count(i))
list_two = zip(str_list_single, num_list)
entropy = 0
for j in range(len(list_two)):
    entropy += -1 * (float(list_two[j][1] / n)) * math.log(float(list_two[j][1] / n), 2)
if len(str(entropy).split('.')[-1]) >= 7:
    print('%.7f' % entropy)
else:
    print(entropy)