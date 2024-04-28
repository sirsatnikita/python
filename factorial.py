# n= int(input("Enter the value of n :-"))
# f=1
# i=1
# while i<=n:
# 	f=f*i
# 	i=i+1
# else:
# 	print(f)
# def factorial(n):
#     if n == 0 :
#         return 1
#     else:
#         return n * factorial(n-1)
# num=5
# print("Factorial of", num, "is", factorial(num))

# N=int(input("Enter the num"))
# for i in range(N):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# N=int(input("Enter the num"))
# for i in range(N):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# def square (x):
#     squ = x*x
#     print(squ)
# num=int(input("Enter the value :- "))
# square(num)
# def calculation (x=3,y=4,z=8):
#     data = x+y+z
#     return data
# print (calculation(6,8,9))
# print (calculation(6,8))
# print (calculation(6))
# def calculation(x):
#     squ=x**2
#     cube=x**3
#     return squ,cube
# num = int(input("enter the value :- "))
# x,y=calculation(num)
# print (calculation(x))
# print (calculation(y))
# def calculation(x):
#     squ = x ** 2
#     cube = x ** 3
#     return squ, cube

# num = int(input("Enter the value: "))
# x, y = calculation(num)
# print("Squared:", x)
# print("Cubed:", y)

# def array(arr):
#     sum_val = sum(arr)
#     avg_val = sum_val / len(arr)
#     return sum_val, avg_val

# arr = [23, 3, 45, 21, 34, 52, 27]
# a, b = array(arr)
# print("Addition is", a)
# print("Average is %.2f" % b)

# data = [23,34,12,13,14,15]
# result = filter(lambda x: x>15,data)
# print (list(result)) 
# my_set = set([1, 2, 3, 4, 5,5,4,3])
# print(my_set)
def is_leap_year(year):
    if (year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False
year=int(input("enter the value"))
if is_leap_year(year):
    print(year,"this is a leap")
else:
    print(year,"not leap")


