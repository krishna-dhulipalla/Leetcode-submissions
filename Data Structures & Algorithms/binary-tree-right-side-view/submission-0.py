class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            # First time we reach this depth → add to res
            if depth == len(res):
                res.append(node.val)

            # Go right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
