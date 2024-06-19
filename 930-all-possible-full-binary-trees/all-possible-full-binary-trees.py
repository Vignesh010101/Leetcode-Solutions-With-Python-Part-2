# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from functools import lru_cache
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def recurse(count):
            if count == 1: return [TreeNode()]
            output = []
            for i in range((count - 1) // 2):
                l_output, r_output = recurse(i * 2 + 1), recurse(count - 2 - i * 2)
                for j in range(len(l_output)):
                    for k in range(len(r_output)):
                        output.append(TreeNode(val=0, left=l_output[j], right=r_output[k]))
            return output
        return recurse(n)