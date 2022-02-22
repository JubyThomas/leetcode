import math   
        
nums = [3,2,3]

majority_elem=math.ceil(len(nums)/2)
result = {}
#print(majority_elem)
        
for i in nums:            
            #if(nums.count(i)>=majority_elem):
    if i in result :
        result[i]+=1
    else:
        result[i]=1
                
for key,val in result.items():
    if val>= majority_elem:
        print(key)