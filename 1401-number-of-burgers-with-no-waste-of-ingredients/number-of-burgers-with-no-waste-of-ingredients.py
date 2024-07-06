class Solution:
    def numOfBurgers(self, t: int, c: int) -> List[int]:
        if t % 2 != 0: # its odd then 1 tomato will always be remaining
          return []
        totalJumbo = t // 4
        left = 0
        right = totalJumbo
        while left < right:
            mid = (left + right) // 2
            remaining = t - (4 * mid)
            totalSmall = remaining / 2
            burgerPossible = mid + totalSmall
            if burgerPossible == c:
                return [mid, int(totalSmall)]
            elif (burgerPossible) < c: # we are making more jumbo reduce it 
                right = mid
            else:
                left = mid + 1
        remaining = t - (4 * left)
        Small = remaining / 2
        if left + Small == c:
            return [left, int(Small)]
        return []