# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = deque()
        if root:
            root.val = 0
        else:
            return

        que.append(root)
        prev_parent = []
        while que:
            sum_row = 0
            loc_parent = []
            for _ in range(len(que)):
                node = que.popleft()
                sum_row+=node.val
                loc_parent.append(node)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if prev_parent:
                for parent in prev_parent:
                    left = parent.left.val if parent.left else 0
                    right = parent.right.val if parent.right else 0
                    if parent.left:
                        parent.left.val = sum_row-(left+right)
                    if parent.right:
                        parent.right.val = sum_row-(left+right)
            prev_parent = loc_parent
        return root

        return root        



        