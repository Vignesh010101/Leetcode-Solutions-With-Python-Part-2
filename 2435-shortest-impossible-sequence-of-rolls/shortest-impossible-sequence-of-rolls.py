class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        cnt = 1
        seen = set()
        for i in range(len(rolls)):
            seen.add(rolls[i])
            if len(seen) == k:
                seen = set()
                cnt += 1
        return cnt