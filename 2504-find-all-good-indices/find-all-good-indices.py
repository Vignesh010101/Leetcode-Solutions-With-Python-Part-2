class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        ans = []

        if n == 3:

            return [1]

        if k == 1:

            for i in range(1, n - 1):

                ans.append(i)

            return ans

        left = set()

        right = set()

        for i in range (k - 1):

            if nums[i] < nums[i + 1]:

                left.add(i)

        for i in range(k + 1, 2 * k):

            if i + 1 >= n:
                
                break

            if nums[i] > nums[i + 1]:

                right.add(i)

        for i in range(k, n - k + 1):

            if i + k >= n:

                break

            if len(left) == 0 and len(right) == 0:

                ans.append(i)

            if i - k in left:

                left.remove(i - k)

            if i + 1 in right:

                right.remove(i + 1)

            if nums[i] > nums[i - 1]:

                left.add(i - 1)

            if i + k + 1 < n and nums[i + k] > nums[i + k + 1]:

                right.add(i + k)

            
        return ans