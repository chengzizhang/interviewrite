def count(a):
    list1=[]
    suma=0
    i=2
    s=0
    ss=1
    while suma<a and i<a-suma+1:

        suma=suma+i
        list1.append(i)
        i=i+1
    l=a-suma
    if l==0:
        while s<len(list1):
            ss=ss*list1[s]
            s=s+1
        print(ss)
    else:


        i=i-1
        j=i
        while l>0 and j>0:
            list1[j-2]=list1[j-2]+1
            j=j-1
            l=l-1
        c=0
        sumb=1
        while c<len(list1):
            sumb=sumb*list1[c]
            c=c+1
        print(sumb)
a=input()
a=int(a)
count(a)