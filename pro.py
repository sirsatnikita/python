n= int(input("Enter the value of n :-"))
mul=1
while n>0:
	r=n%10
	mul=mul*r
	n=n//10
else:
	print(mul)
