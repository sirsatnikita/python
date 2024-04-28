#num1 = float(input())
#num3 = float(input())

#if num1>=num2 and num1>=num3:
	#second_max = (num2,num3)
	
#elif num2>=num1 and num2>=num3:
	#second_max = (num1,num3)
	
#else:
	#second_max = (num1,num2)
 	
#print("the second max number is :",second_max)#


# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the second maximum
if num1 >= num2 and num1 >= num3:
    second_max = max(num2, num3)
elif num2 >= num1 and num2 >= num3:
    second_max = max(num1, num3)
else:
    second_max = max(num1, num2)

print("The second max number is:", second_max)

