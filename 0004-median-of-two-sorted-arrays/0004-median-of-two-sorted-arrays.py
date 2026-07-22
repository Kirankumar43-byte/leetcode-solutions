class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=sorted(nums1+nums2)
        n=len(num3)
        mid=n//2
        if n%2==0:
            return(num3[mid-1]+num3[mid])/2
        else:
            return num3[mid]
