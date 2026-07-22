class Solution:
    def permute(self, a: List[int]) -> List[List[int]]:
        return [*permutations(a)]