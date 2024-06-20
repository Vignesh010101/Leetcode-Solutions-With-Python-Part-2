class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1, cnt2 = Counter(basket1), Counter(basket2)
        minCost = min(min(basket1), min(basket2)) * 2
        move1, move2 = [], []
        for fruit in cnt1:
            if (cnt1[fruit] + cnt2[fruit]) % 2 != 0:
                return -1
            avgFruit = (cnt1[fruit] + cnt2[fruit]) // 2
            if cnt1[fruit] > avgFruit:
                move1 += [fruit] * (cnt1[fruit] - avgFruit)
        for fruit in cnt2:
            if (cnt1[fruit] + cnt2[fruit]) % 2 != 0:
                return -1
            avgFruit = (cnt1[fruit] + cnt2[fruit]) // 2
            if cnt2[fruit] > avgFruit:
                move2 += [fruit] * (cnt2[fruit] - avgFruit)
        move1.sort()
        move2.sort()
        ans, m = 0, len(move1)
        for i in range(m):
            ans += min(min(move1[i], move2[m - 1 - i]), minCost)
        return ans