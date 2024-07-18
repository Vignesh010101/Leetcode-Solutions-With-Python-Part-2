# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,larger):
            nonlocal res
            if not root:return

            if root.val>=larger:
                res+=1
            larger=max(larger,root.val)
            dfs(root.left,larger)
            dfs(root.right,larger)

        res=0
        dfs(root,root.val)
        return res