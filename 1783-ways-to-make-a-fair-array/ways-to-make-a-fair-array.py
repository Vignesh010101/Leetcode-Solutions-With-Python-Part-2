class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_sum = 0
        odd_sum = 0
        for i, num in enumerate(nums):
            if i%2 == 0:
                even_sum += num
            else:
                odd_sum += num

        num_indices = 0
        cur_even_sum = 0
        cur_odd_sum = 0
        for i, num in enumerate(nums):

            even = 2* cur_even_sum - even_sum
            odd = 2* cur_odd_sum - odd_sum

            if i%2 == 0:
                even = even + num
            else:
                odd = odd + num

            if even == odd:
                num_indices += 1

            if i%2 == 0:
                cur_even_sum += num
            else:
                cur_odd_sum += num
            
        return num_indices
            
            
            
            




        