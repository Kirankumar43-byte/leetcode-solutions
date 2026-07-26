class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        arr=[]
        for row in grid:
            arr+=row
        k%=len(arr)    
        arr=arr[-k:]+arr[:-k]     
        res=[]
        idx=0
        for i in range(m):
            res.append(arr[idx:idx+n])
            idx+=n  
        return res