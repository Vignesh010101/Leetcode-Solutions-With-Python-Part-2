# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        no_avg = 0
        def dfs(head):
            tot = 0
            count = 0
            nonlocal no_avg
            if head:
                a, b = dfs(head.left)
                x, y = dfs(head.right)
                tot += a + x + head.val
                count += 1 + b + y
                if tot//count == head.val:
                    no_avg += 1
                return tot, count
            return 0, 0
        dfs(root)
        return no_avg