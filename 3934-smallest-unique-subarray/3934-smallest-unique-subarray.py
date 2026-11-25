class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        b, m1, m2 = 101, 10**9 + 7, 10**9 + 9
        h1, h2 = [0]*(n+1), [0]*(n+1)
        p1, p2 = [1]*(n+1), [1]*(n+1)
        for i in range(n):
            h1[i+1] = (h1[i]*b + nums[i]) % m1
            h2[i+1] = (h2[i]*b + nums[i]) % m2
            p1[i+1] = p1[i]*b % m1
            p2[i+1] = p2[i]*b % m2
        def check(k):
            count = {}
            for i in range(n-k+1):
                x = (h1[i+k] - h1[i]*p1[k]) % m1
                y = (h2[i+k] - h2[i]*p2[k]) % m2
                key = (x, y)
                count[key] = count.get(key, 0) + 1
            return 1 in count.values()
        l, r = 1, n
        while l < r:
            mid = (l+r)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l