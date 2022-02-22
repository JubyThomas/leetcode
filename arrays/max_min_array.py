from cmath import inf


arr=[12,89,87,54,87,66]
minx=arr[0]
maxx=arr[0]
for i in range(1,len(arr)-1):
    if(arr[i]<minx):
        minx=arr[i]
    elif(arr[i]>maxx):
        maxx=arr[i]
        
print(minx,maxx)        
        