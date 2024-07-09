class Solution:
    def numTeams(self, rating: List[int]) -> int:
        dp = []
        for i in range(len(rating)):
            dp.append([0, 0, 0, 0])
        for i in range(len(rating) - 1, -1, -1):
            for j in range(i + 1, len(rating)):
                if rating[j] < rating[i]:
                    dp[i][1] += dp[j][0]
                    dp[i][0] += 1
                elif rating[j] > rating[i]:
                    dp[i][3] += dp[j][2]
                    dp[i][2] += 1
        return sum([dp[i][1] + dp[i][3] for i in range(len(dp))])      