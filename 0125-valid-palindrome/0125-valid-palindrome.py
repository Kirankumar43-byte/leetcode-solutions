class Solution(object):
    def isPalindrome(self, s):
        org = []
        for i in s:
            if i.isalnum():
                org.append(i.lower())
        return org == org[::-1]
