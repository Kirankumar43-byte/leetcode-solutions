class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return min(int(dividend/divisor),2**31-1)