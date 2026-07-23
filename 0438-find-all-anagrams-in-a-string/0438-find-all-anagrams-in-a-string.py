class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count=Counter(p)
        return [i for i in range(len(s)-len(p)+1) if Counter(s[i:i+len(p)])==count]