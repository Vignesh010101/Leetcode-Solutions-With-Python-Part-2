class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        A & B <= A, B
        """
        max_num = max(nums)
        continous_num = 0
        max_continous_num = 0
        for i, val in enumerate(nums):
            if val == max_num:
                continous_num += 1
                max_continous_num = max(max_continous_num, continous_num)
            else:
                continous_num = 0
        return max_continous_num
                

        