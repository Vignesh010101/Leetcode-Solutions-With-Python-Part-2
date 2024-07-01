class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n, mx, mod = len(nums), max(nums), 10**9+7
        maxGap, ttlGap = mx-min(nums), mx*n-sum(nums)
        
        if cost1*2 <= cost2:
            # Easy case, Op 1
            return ttlGap*cost1 % mod
        
        if maxGap*2 <= ttlGap:
            # The maxGap is less than a half of ttlGap, we can always find pairs for Op 2
            res =  ttlGap // 2 * cost2
            if ttlGap % 2 == 1:
                # Corner case with the last one spot left
                if n % 2 == 1:
                    res += min(cost1, cost2 * (n+1) // 2)
                else:
                    res += cost1
            return res % mod
        
        # Two Operations:
        #   Op 1: Directly fill maxGap
        #   Op 2: Pair maxGap with other nums, which increases the final level.

        res = cost2 * (ttlGap - maxGap)
        maxGap -= ttlGap - maxGap

        if maxGap >= n-1:
        
            if cost2 * (n-1) >= cost1 * (n-2):
                # Op 1 is better
                res += maxGap // (n-1) * (n-1) * cost1
                maxGap %= n-1
            else:
                # Op 2 is better
                res += maxGap // (n-2) * (n-1) * cost2
                maxGap %= n-2

        if maxGap:
            # For the last round, Op 2: Increase the level by 1 to get (n+maxGap)//2 pairs
            op2 = (n+maxGap) // 2 * cost2 # = (maxGap + (n-maxGap)//2) * cost2
            if (n+maxGap) % 2 == 1:
                # The last one spot left
                if n%2 == 1:
                    op2 += min(cost1, cost2*(n+1)//2)
                else:
                    op2 += cost1

            # Compare it with Op 1 
            res += min(op2, maxGap * cost1)

        return res % mod