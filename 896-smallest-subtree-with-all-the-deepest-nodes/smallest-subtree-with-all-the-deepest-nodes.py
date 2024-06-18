# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lca(self, root, p, q):
        if root in (None, p, q): return root
        l = self.lca(root.left, p, q)
        r = self.lca(root.right, p, q)
        return root if l and r else l or r
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        a = []
        def dfs(node, h):
            if not node:
                return
            if len(a) == h:
                a.append([])
            a[h].append(node)
            dfs(node.left, h+1)
            dfs(node.right, h+1)
        dfs(root, 0)
        p, q = a[-1][0], a[-1][-1]
        return self.lca(root, p, q)        