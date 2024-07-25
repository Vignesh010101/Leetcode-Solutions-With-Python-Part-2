class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        result=1
        for coin in coins:
            if result-coin<0:
                break
            result+=coin
        return result