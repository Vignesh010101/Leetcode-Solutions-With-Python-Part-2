# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque()
        q.append(root)
        head = root
        count = 0
        arr = []
            
        while q: 
            for _ in range(len(q)):
                cur = q.popleft()
                
                if cur.left: 
                    if count %2 == 0:
                        arr.append(cur.left.val)
                        arr.append(cur.right.val)  
                    else:
                        cur.val = arr[-1]
                        arr.pop()
                
                    q.append(cur.left)
                    q.append(cur.right)
                    
                elif cur and arr: 
                     
                    cur.val = arr[-1]
                    arr.pop()
                
                    
            count += 1 
            
        return head 
            
        
        