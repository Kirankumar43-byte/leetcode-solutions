class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        last = [-1] * 26
        new = [[] for _ in range(n)]
        def dfs(u):
            c = ord(s[u]) - 97
            old = last[c]
            p = old if old != -1 else parent[u]
            if u:
                new[p].append(u)
            last[c] = u
            for v in children[u]:
                dfs(v)
            last[c] = old
        dfs(0)
        ans = [1] * n
        def calc(u):
            for v in new[u]:
                calc(v)
                ans[u] += ans[v]
        calc(0)
        return ans

