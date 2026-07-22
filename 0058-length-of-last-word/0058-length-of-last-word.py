class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_length=s.split()
        return (len(last_length[-1]))