class Solution:
    def digArtifacts(self, n, artifacts, dig):

        dig = set((r,c) for r,c in dig)

        count =0
        for r1,c1, r2,c2 in artifacts:
            positions = set()
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    positions.add((r,c))

            if all([pos in dig for pos in positions]):
                count+=1

        return count