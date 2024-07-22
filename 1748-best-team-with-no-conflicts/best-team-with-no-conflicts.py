from typing import List

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.sums[i] = max(self.sums[i], delta)
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans = max(ans, self.sums[i])
            i -= i & -i
        return ans

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageScorePair = [(a, s) for a, s in zip(ages, scores)]
        ageScorePair.sort(key=lambda x: (x[1], x[0]))
        highestAge = max(ages)
        BIT = BinaryIndexedTree(highestAge + 1)
        ans = 0
        for i in range(len(ageScorePair)):
            age, score = ageScorePair[i]
            j = BIT.query(age)
            ans = max(ans, j + score)
            BIT.update(age, j + score)
        return ans