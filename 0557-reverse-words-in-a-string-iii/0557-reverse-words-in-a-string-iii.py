class Solution:
    def reverseWords(self, s: str) -> str:
        rev = s.split()
        for i in range (len(rev)):
            rev[i] = rev[i][::-1]
        return ' '.join(rev)   