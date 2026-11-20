class Solution(object):
    def topKFrequent(self, nums, k):
        d={}
        l=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        new = sorted(d, key=d.get, reverse=True)
        return new[:k]