class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dig = set((r, c) for r, c in dig)
        ans = 0
        for r0, c0, r1, c1 in artifacts:
            if all((r, c) in dig for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)):
                ans += 1
        return ans