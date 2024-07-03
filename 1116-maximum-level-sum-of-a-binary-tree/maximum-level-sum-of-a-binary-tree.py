# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack, sums = [(root, 0)], defaultdict(int)

        while stack:
            curr, lvl = stack.pop()

            sums[lvl] += curr.val

            if curr.left:
                stack.append([curr.left, lvl+1])
            if curr.right:
                stack.append([curr.right, lvl+1])
        
        return next(filter(lambda kv: max(sums.values()) == kv[1], sums.items()))[0] + 1
        