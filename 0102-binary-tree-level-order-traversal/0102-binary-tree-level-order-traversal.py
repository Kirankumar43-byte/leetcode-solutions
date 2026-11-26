class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def bfs(curr = root, level = 0):
            nonlocal ans
            if curr:
                if len(ans) > level:
                    ans[level].append(curr.val)
                else:
                    ans.append([curr.val])
                bfs(curr.left, level + 1)
                bfs(curr.right, level + 1)
            return
        bfs()
        return ans