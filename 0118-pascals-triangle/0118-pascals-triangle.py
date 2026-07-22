class Solution:
    def generate(self, n: int) -> List[List[int]]:
        return [[comb(i,j) for j in range(i+1)] for i in range(n)]