sp,cp = map(int,input().split())

if(sp==cp):
	print("no profit/no loss")
	
elif(sp>cp):
	print("profit")
	
else:
	print("loss")
