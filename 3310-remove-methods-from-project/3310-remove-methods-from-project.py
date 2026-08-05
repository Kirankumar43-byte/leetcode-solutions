class Solution:
    def dfs(self, node, adj, vis):
        vis[node] = True
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it, adj, vis)
    def remainingMethods(self, n, k, nums):
        adj = [[] for _ in range(n)]
        for it in nums:
            adj[it[0]].append(it[1])
        vis = [False] * n
        self.dfs(k, adj, vis)
        ans = []
        flag = True
        for i in range(n):
            if not vis[i]:
                for it in adj[i]:
                    if vis[it]:
                        flag = False
        if flag:
            ans = [i for i in range(n) if not vis[i]]
        else:
            ans = list(range(n))
        return ans