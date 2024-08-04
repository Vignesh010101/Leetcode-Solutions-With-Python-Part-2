class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        vacant = []
        for a, b in zip(capacity, rocks):
            vacant.append(a - b)

        vacant.sort()
        ans = 0

        for i in range(len(vacant)):
            if vacant[i] == 0:
                ans += 1
            else:
                if additionalRocks >= vacant[i]:
                    additionalRocks -= vacant[i]
                    ans += 1
                else:
                    break
        return ans