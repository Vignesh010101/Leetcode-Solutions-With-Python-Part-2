class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        i = 0
        num_deletions = 0
        while i < n - 1:
            if nums[i] == nums[i+1]:
                cur_pos = i+1
                while cur_pos < n and nums[cur_pos] == nums[i]:
                    num_deletions += 1
                    cur_pos += 1
                i = cur_pos + 1
            else:
                i += 2
        if (n % 2 == 1) ^ (num_deletions % 2 == 1):
            return num_deletions + 1
        return num_deletions