# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_map = defaultdict(int)
        level_map[-1] = root.val
        q = deque([root])
        level = -1
        while len(q):
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    level_map[level] += node.left.val
                    q.append(node.left)

                if node.right:
                    level_map[level] += node.right.val
                    q.append(node.right)

        # level 0 and level 1 will always be zero
        root.val = 0
        level = -1
        q = deque([root])
        while len(q):
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                node_child_sum = 0
                if node.left:
                    node_child_sum += node.left.val
                if node.right:
                    node_child_sum += node.right.val

                if node.left:
                    node.left.val = level_map[level] - node_child_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = level_map[level] - node_child_sum
                    q.append(node.right)
        return root   