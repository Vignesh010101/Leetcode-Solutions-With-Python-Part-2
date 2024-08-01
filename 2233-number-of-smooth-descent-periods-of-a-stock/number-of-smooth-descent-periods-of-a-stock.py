class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 1
        sol, rem, after, not_visited = 0, 0, 0, True
        for i in range(len(prices)-1):
            if prices[i] - prices[i+1] == 1:
                rem += 1
                not_visited = False
            else:
                if rem >= 1:
                    rem += 1
                    sol += ((rem * (rem + 1)) // 2)
                else:
                    after += 1
                rem = 0
        if rem >= 1: 
            rem += 1
            sol += ((rem * (rem + 1)) // 2)
        if len(prices) >= 2 and prices[-2] - prices[-1] != 1:
            after += 1 
        return sol + after