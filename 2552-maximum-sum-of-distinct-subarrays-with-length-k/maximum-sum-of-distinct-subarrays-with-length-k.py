class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        def sliding_window(nums, k):
            max_sum = 0
            current_sum = 0
            num_set = set()
            left = 0

            # Iterate over elements in our input
            for right in range(len(nums)):
                # Expand the window
                while nums[right] in num_set:
                    num_set.remove(nums[left])
                    current_sum -= nums[left]
                    left += 1

                num_set.add(nums[right])
                current_sum += nums[right]

                if right - left + 1 == k:
                    max_sum = max(max_sum, current_sum)
                    num_set.remove(nums[left])
                    current_sum -= nums[left]
                    left += 1

            return max_sum        
        return sliding_window(nums, k)