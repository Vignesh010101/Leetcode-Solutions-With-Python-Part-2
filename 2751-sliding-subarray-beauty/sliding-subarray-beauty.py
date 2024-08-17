from sortedcontainers import SortedList
from collections import deque

class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ret = []
        left = 0
        currWindow = deque()
        currNegativeNums = SortedList()
        
        for right in range(n):
            num = nums[right]
            currWindow.append(num)
            if num < 0:
                currNegativeNums.add(num)

            if right - left + 1 > k:
                removedNum = currWindow.popleft()
                if removedNum < 0:
                    currNegativeNums.remove(removedNum)
                left += 1

            if right - left + 1 == k:
                if len(currNegativeNums) < x:
                    ret.append(0)
                else:
                    ret.append(currNegativeNums[x - 1])
        
        return ret