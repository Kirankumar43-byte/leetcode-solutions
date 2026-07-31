class Solution:
    def minimumPushes(self, s: str) -> int:
        return sum((i//8+1)*f for i,(_,f) in enumerate(Counter(s).most_common()))