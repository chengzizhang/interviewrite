
a=[10,2,2,10]
d=[]
d[0]=a[3]
for b in range(1,a[0]):
	d[b]=(d[b-1]+153)%(d[0])
for i in range(1,a[1]+1):
	for j in range(1,a[2]+1):
    	suma=suma+d[gcm(j,i)]
        print(suma)
def gcm(a, b):
    if a >= b:
        if a % b == 0:
            return b
        else:
            return gcm(b, a - b)
    else:
        return gcm(b, a)
def binarytree():
    visit(node)
    if n!=null:
        visit(father.node)
        visit(leftchild.node)
        visit(rightchild.node)
        return 0
    else:
        break
def hashtree():
    
