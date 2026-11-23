class Solution:
    def validPath(self, n, edges, source, destination):
        G = [[] for _ in range(n)]
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for i in G[node]:
                if i not in visited:
                    if dfs(i):
                        return True
            return False
        return dfs(source)