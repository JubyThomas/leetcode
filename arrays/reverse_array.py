arr=[12,89,87,54,87,66]


newarr=[]
for item in reversed(arr):
    newarr.append(item)
print(newarr)

#Double Colon operator or extended slicing :: 
print(arr[::-1])

n=len(arr)-1
out=[]
while n>=0:
    out.append(arr[n])
    n-=1
    
print("out without inbuilt function",out)    
