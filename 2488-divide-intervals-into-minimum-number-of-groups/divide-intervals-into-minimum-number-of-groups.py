class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        line = []
        for x, y in intervals: 
            line.append((x, 1))
            line.append((y+1, 0))
        ans = prefix = 0 
        for x, k in sorted(line): 
            if k: prefix += 1
            else: prefix -= 1
            ans = max(ans, prefix)
        return ans 