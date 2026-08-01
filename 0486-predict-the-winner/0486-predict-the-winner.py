class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(nums,fl):
            return 0 if not nums else (max(nums[0] - rec(nums[1:],False),nums[-1]- rec(nums[:len(nums)-1],False)) if fl else max(nums[0] - rec(nums[1:],True),nums[-1]- rec(nums[:len(nums)-1],True)))
        return rec(nums,True) >= 0
                