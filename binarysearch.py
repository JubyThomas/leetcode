mylist=[2,7,1,8,9,6,4]

target=12

def binarySearch(mylist,target):
    left, right = 0, len(mylist) - 1 
    while left <= right:
        mid = (left + right) // 2
		if nums[mid]==target:
           return mid
        elif(nums[mid] < target):
           left = mid + 1
        else:
           right = mid - 1
	return -1