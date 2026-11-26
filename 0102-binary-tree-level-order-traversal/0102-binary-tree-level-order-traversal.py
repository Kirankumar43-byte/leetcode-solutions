class Solution:
    def levelOrder(self, root):
        ans = []
        def dfs(curr, level):
            if curr:
                if len(ans) <= level:
                    ans.append([])
                ans[level].append(curr.val)
                dfs(curr.left, level + 1)
                dfs(curr.right, level + 1)
        dfs(root, 0)
        return ans