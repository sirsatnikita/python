sp,cp = map(int,input().split())
if(sp>cp):
	p=sp-cp
	per=(p//cp)*100
	print(p-per)
	
else:
	print("invalid")
