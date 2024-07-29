class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        odd = [0]
        even = [1]
        for i in range(1, len(nextVisit)): 
            odd.append((even[-1] + 1) % 1_000_000_007)
            even.append((2*odd[-1] - odd[nextVisit[i]] + 1) % 1_000_000_007)
        return odd[-1] 