class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        k = 0
        c = Counter(tasks).values()
        if 1 in c:
            return -1
        for j in c:
            k += j // 3 + bool(j % 3)
        return k