"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def order(root):
            if root is None: return None
            for i in root.children:
                order(i)
            res.append(root.val)

        order(root)
        return res