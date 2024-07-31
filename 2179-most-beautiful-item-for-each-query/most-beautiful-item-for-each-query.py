class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        ans = [0]*len(queries)
        prefix = ii = 0 
        for x, i in sorted((x, i) for i, x in enumerate(queries)): 
            while ii < len(items) and items[ii][0] <= x: 
                prefix = max(prefix, items[ii][1])
                ii += 1
            ans[i] = prefix
        return ans 