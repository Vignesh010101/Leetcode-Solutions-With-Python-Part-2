class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        intervals = []
        max_beffore = []
        start_inx = 0
        count = 0
        for inx, pos in enumerate(prizePositions):
            count += 1
            while pos-k > prizePositions[start_inx]:
                count -= 1
                start_inx += 1
            intervals.append((count, pos))
            if not max_beffore or max_beffore[-1][0] < count:
                max_beffore.append((count, pos))

        max_solution = 0
        while intervals:
            count, pos = intervals.pop()
            while max_beffore and max_beffore[-1][1] >= pos-k:
                max_beffore.pop()
            candidate = count + (0 if not max_beffore else max_beffore[-1][0])
            max_solution = max(candidate, max_solution)
        return max_solution
