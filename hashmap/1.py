from unittest import result


nums = [3,2,4]
target = 6


hash_map = {}
        
for index, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                print( [hash_map[complement], index])
            else:
                hash_map[num] = index
                
print(hash_map)                