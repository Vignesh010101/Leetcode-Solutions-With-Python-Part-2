class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ll = sorted([[nums[i], cost[i]] for i in range(len(cost))])
        c = list(accumulate([ll[i][1] for i in range(len(cost))]))
        nc = list(accumulate([ll[i][0] * ll[i][1] for i in range(len(cost))]))
        return min([ll[i][0]*(2*c[i]-c[len(cost)-1]) + (nc[len(cost)-1]-2*nc[i]) for i in range(len(cost))])