# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import defaultdict

        count = defaultdict(int)
    
        for x in arr:
            count[x] += 1

        distinct = [x for x in count if count[x] == 1]

        if k <= len(distinct):
            return distinct[k - 1]
    
        return ""       