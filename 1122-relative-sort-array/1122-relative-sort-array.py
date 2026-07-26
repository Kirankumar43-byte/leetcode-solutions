class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=sorted(arr1)
        b=((arr2+a).index)
        return sorted(a,key=b)