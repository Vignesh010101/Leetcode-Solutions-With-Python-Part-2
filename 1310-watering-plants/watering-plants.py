class Solution:
    def wateringPlants(self, plants: List[int], c: int) -> int:
        i = 0
        steps = 0
        org = c
        while i <= len(plants)-1:
            if c >= plants[i]:
                steps += 1
                c -= plants[i]
            else:
                c = org
                steps += (i+1)*2 - 1
                c -= plants[i]
            i += 1
        return steps