def  find_maximum(a, b, c):
    max_num = max(a, b, c)
    #return max_num

num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
num3 = int (input("Enter the third number: "))

maximum = find_maximum(num1, num2, num3)
print("The maximum number is:", maximum)

