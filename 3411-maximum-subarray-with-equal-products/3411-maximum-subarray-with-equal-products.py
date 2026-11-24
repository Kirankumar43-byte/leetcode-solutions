from math import gcd
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            p, g, l = 1, 0, 1
            for j in range(i, len(nums)):
                x = nums[j]
                p *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if p == l * g:
                    ans = max(ans, j-i+1)
        return ans