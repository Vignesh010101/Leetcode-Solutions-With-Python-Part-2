class Solution:
    def numMovesStonesII(self, stones: list[int]) -> list[int]:
        A, N = sorted(stones), len(stones)
        maxMoves = max(A[N - 1] - A[1] - N + 2, A[N - 2] - A[0] - N + 2)
        minMoves = N

        # Calculate minimum moves through sliding window.
        start = 0
        for end in range(N):
            while A[end] - A[start] + 1 > N:
                start += 1

            if end - start + 1 == N - 1 and A[end] - A[start] + 1 == N - 1:
                # Case: N - 1 stones with N - 1 positions.
                minMoves = min(minMoves, 2)
            else:
                minMoves = min(minMoves, N - (end - start + 1))

        return [minMoves, maxMoves]