class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        s = []
        r = [0]*len(T)
        for i,t in enumerate(T):
            while s and T[s[-1]] < t:
                r[s.pop()] = i - s[-1]
            s.append(i)
        return r