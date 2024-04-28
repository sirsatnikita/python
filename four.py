a,b,c,d = map(int,input().split())

if a>b:
	max1=a
	smax1=b
	
else:
	max1=b
	smax1=a
	
if c>d:
	max2=c
	smax2=d
	
else :
	max2=d
	smax2=c
	
if max1>max2:
	if max1>smax1:
		print(max1)
	
	else:
		print(smax1)
		
else:
	
	if max2>smax2:

		print(max2)
	
	else:
		print(smax2)

