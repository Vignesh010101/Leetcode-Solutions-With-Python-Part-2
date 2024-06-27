class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total/2
        dp = set([0])

        for stone in stones:
            nextDp = dp.copy()
            for val in dp:
                if stone+val==target:
                    return 0
                elif stone+val<target:
                    nextDp.add(stone+val)
            dp = nextDp

        firstStone = max(dp)
        secondStone = total-max(dp)
        return abs(firstStone-secondStone)