a=input("请输入：")
b=[]
c=[]
d=[]
for i in range(1,10):
    if str(i) not in a:
        b.append(i)
    else:
        continue
if len(b):
    print(min(b))
elif '0' not in a:
    for k in a:
        c.append(int(k))
    print(min(c)*10)
else:
    for m in a:
        c.append(int(m))
    for s in range(0,10):
        d.append(c.count(s))
    q=min(d)
    f=d.index(min(d))
    suma = 10 ** (q + 1)
    while q!=-1:
        suma=suma+f*(10**q)
        q=q-1
    print(suma)
