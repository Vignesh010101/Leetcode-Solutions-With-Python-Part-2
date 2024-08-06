from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(num1 - num2) for num1, num2 in zip(nums1, nums2)]

        k = k1+ k2
        if sum(diff) <= k: return 0

        diffCount = Counter(diff)
        diff = sorted(diffCount.keys(), reverse = True)
        n = len(diff)

        i = 0; count = diffCount[diff[i]]

        while i+1 < n and (diff[i] - diff[i+1])*count <= k:
            k -= (diff[i] - diff[i+1])*count
            count += diffCount[diff[i+1]]
            i += 1

        def findResidualSum(k, num, count):
            if k >= num*count: return 0

            k, num = k%count, num - k//count
            ret = k*(num-1)**2 + (count-k)*num**2
            return ret

        res = findResidualSum(k, diff[i], count)
        ret = res + sum([diffCount[d]*d**2 for d in diff[i+1:]])
        return ret