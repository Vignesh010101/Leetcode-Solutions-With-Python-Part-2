class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        sum = 0
        number = 0
        for i in range(1, n+1):
            if i not in ban:
                sum += i
                if sum <= maxSum:
                    number += 1
                else:
                    return number
        return number