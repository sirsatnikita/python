arr =[5,2,8,9,3,7]
n=len(arr)
for i in range(n):
	for j in range(0,n-i-1):
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
