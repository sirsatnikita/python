#uses of lambda function ?
#lambda function use for small code like find the even number, odd number etc..
#lambda function is a small  anonymous function 

# num = [20,45,60,67,22,44]
# evens= list(filter(lambda x:x % 2==0,num ))
# print(evens)

'''def Myfunc(n):
    return lambda a : a * n 
myclass =Myfunc(10)
print(myclass(11))'''
def Myfunc(n):
    return lambda a:a*n
myclass = Myfunc(2)
mysub = Myfunc(3)

print(myclass(11))
print(mysub(11))