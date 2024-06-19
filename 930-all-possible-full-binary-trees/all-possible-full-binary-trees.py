# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import deepcopy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        ans = []
        if not n % 2: # impossible to produce even num full tree
            return ans
        # combinatorial search with backtracking, at each step either set two children or set 0 children
        def generate_trees(n, node, unprocessed):
            if n == 0:
                ans.append(deepcopy(head))
                return
            node.left = TreeNode()
            node.right = TreeNode()
            unprocessed.append(node.left)
            unprocessed.append(node.right)
            # go over every combination of dfs expansion based on unprocessed candidates
            for ind, next_node in enumerate(unprocessed):
                generate_trees(n - 2, next_node, unprocessed[ind+1:])
                next_node.left = next_node.right = None # backtrack
                if n - 2 == 0: return # don't double count dups
        head = TreeNode()
        unprocessed = []
        generate_trees(n-1, head, unprocessed)
        return ans  