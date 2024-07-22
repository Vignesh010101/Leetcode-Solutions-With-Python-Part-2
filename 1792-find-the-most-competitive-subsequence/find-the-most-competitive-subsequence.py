class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans, pq = [], []
        prev = -inf 
        for i, x in enumerate(nums): 
            heappush(pq, (x, i))
            if i+k >= len(nums): 
                while pq and pq[0][1] < prev: heappop(pq)
                x, prev = heappop(pq)
                ans.append(x)
        return ans 