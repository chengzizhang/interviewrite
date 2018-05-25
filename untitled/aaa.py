while 1:
    a = []
    s = input()


    a.append(s)


a.pop(a[0])
a.sort()
a.reverse()
for i in a:
    print(i,end = '\n')