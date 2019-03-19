import random

arr = list(range(1,20))
print(arr)
random.shuffle(arr)
print(arr)
j=0
for x in arr:

	
	for y in range(0,len(arr)-1-j):
		print(y)
		print(arr[y], arr[y+1])
		
		if(arr[y]>arr[y+1]):
			temp=arr[y]
			arr[y]=arr[y+1]
			arr[y+1]=temp
		print(arr)
		
	j=j+1
	
print(arr)

input()
