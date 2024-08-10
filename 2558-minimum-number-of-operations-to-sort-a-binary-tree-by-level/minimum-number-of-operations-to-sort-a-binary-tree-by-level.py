# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        stack, cnt = [root], 0
        while stack:
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
            dic_level = {node.val : i for i, node in enumerate(stack)}
            sort_level = sorted(dic_level.keys())
            while dic_level:
                _, i = dic_level.popitem()
                while sort_level[i] in dic_level:
                    i = dic_level.pop(sort_level[i])
                    cnt += 1
        return cnt   