class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        count = [0 for x in range(max(piles) + 1)]
        for x in piles:
            count[x] += 1
        
        for _ in range(k):
            count[-1] -= 1
            count[len(count) // 2] += 1
            while count[-1] == 0:
                count.pop()
        
        return sum(i * count[i] for i in range(len(count)))
