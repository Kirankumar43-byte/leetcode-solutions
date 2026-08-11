class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums) and nums[i] == nums[i-1] + 1:
            i += 1
        prefix_sum = sum(nums[:i])        
        num_set = set(nums)
        while prefix_sum in num_set:
            prefix_sum += 1
        return prefix_sum
