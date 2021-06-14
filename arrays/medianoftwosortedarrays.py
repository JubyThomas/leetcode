from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        mergedList=nums1+nums2
        mergedList.sort()
        mid=len(mergedList)//2 
        print(len(mergedList)//2)
        if(len(mergedList)%2==0):
            print("hii")
            print(mergedList[mid-1])
            print(mergedList[mid]+ mergedList[mid-1]/2)
        else:
            print("hello")
            print(mergedList[mid])


findMedianSortedArrays([1,2],[3,4])           