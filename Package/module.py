def duplicate(l):
    l=[1,2,3,1,2,3,5,7]
    l1=[]
    for i in l:
        if(i not in l1):
            l1.append(i)
    print(l1)
def unique(l):
    l1=[]
    count=0
    for i in l:
        if(l.count(i)==1):
            l1.append(i)
    print(l1)