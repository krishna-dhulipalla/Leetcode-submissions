# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, carry_max):
            if not node:
                return 0

            # is this node good?
            count = 1 if node.val >= carry_max else 0
            # update carry_max for children
            new_max = max(carry_max, node.val)

            # count in both subtrees
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)