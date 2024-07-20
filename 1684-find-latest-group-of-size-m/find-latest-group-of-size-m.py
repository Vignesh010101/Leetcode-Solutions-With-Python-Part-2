BEGIN = 0
END = 1
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n

        ranges = [[1, n]]
        for i in range(-1, -n-1, -1):
            rangeInd = None
            lInd, rInd = 0, len(ranges)-1
            while lInd <= rInd:
                mInd = lInd + (rInd-lInd)//2
                if ranges[mInd][BEGIN] <= arr[i]:
                    rangeInd = mInd
                    lInd = mInd + 1
                else:
                    rInd = mInd - 1

            if arr[i] == ranges[rangeInd][BEGIN] == ranges[rangeInd][END]:
                del ranges[rangeInd]
            elif arr[i] == ranges[rangeInd][BEGIN]:
                ranges[rangeInd][BEGIN] += 1
                if ranges[rangeInd][END] - ranges[rangeInd][BEGIN] + 1 == m:
                    return n - abs(i)
            elif arr[i] == ranges[rangeInd][END]:
                ranges[rangeInd][END] -= 1
                if ranges[rangeInd][END] - ranges[rangeInd][BEGIN] + 1 == m:
                    return n - abs(i)
            else:
                end = ranges[rangeInd][END]
                ranges[rangeInd][END] = arr[i]-1
                ranges.insert(rangeInd+1, [arr[i]+1, end])
                if ranges[rangeInd][END] - ranges[rangeInd][BEGIN] + 1 == m or \
                   ranges[rangeInd+1][END] - ranges[rangeInd+1][BEGIN] + 1 == m:
                    return n - abs(i)
        
        return -1