class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxright=-1
        for i in range(len(arr)-1,-1,-1):
            value=maxright
            maxright=max(maxright,arr[i])
            arr[i]=value
        return arr