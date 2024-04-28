max1=int(input("enter the first number"))
max2=int(input("enter the second number"))
max3=int(input("enter the third number"))

maximun = max (max1,max2,max3)

minimum = min (max1,max2,max3)

second_max = max1+max2+max3-maximun-minimum

print("the second max is",second_max)
