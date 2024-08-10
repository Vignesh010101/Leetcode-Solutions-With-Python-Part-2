# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: TreeNode, queries: List[int]) -> List[List[int]]:
        d, ans = [], []
        def dfs(node):                  
            if not node: return
            dfs(node.left )                                  
            d.append(node.val)
            dfs(node.right)
        dfs(root) 
        for q in queries:        
            idx = bisect_left(d,q)
            if idx == len(d): ans.append([d[-1]   ,-1    ])
            elif d[idx] == q: ans.append([d[idx]  ,d[idx]])
            elif    idx == 0: ans.append([-1      ,d[0]  ])
            else            : ans.append([d[idx-1],d[idx]]) 

        return ans