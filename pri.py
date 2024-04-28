a = [4,2,6,8,1,10,5,3]
m = max(a)
l=[]
for i in range(m):
    c= m-i
    if c in a:
        d = a.index(c)
        l.append(d)
        for j in range(len(a)):
            if (j in l):
                print("*",end="")
            else:
                print("",end=" ")
    else:
        for j in range(len(a)):
            if (j in l):
                print("*",end="")
            else:
                print("",end=" ")
    print()
    
    
