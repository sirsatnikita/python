array=[2, 4, 6, 7,8]
for i in range(0,len(array)):
	key=array[i]
	j=i-1
	while j>=0 and key > array[j]:
		array[j+1]=array[j]
		j-=1
	array[j+1]=key
	
print(array)






