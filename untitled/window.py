
def windows(list1,list2):
    a=1
    for a in range(1,len(list1)-1):
        list2[0]=list1[a-1]
        list2[1]=list1[a]
        list2[2]=list1[a+1]
        print(max(list2))
list1=[-3,32,-2,3,6,2,1]
list2=[1,2,34]
windows(list1,list2)