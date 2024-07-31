class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        si = nums.index(min(nums))  
        li = nums.index(max(nums))
        if si < li:
            if si < len(nums) - li - 1:
                sum = si + 1
                if li - si < len(nums) - li - 1:
                    sum += li - si
                else:
                    sum += len(nums) - li
            else:
                sum = len(nums) - li
                if si < li - si - 1:
                    sum += si + 1
                else:
                    sum += li - si
        else:
            if li < len(nums) - si - 1:
                sum = li + 1
                if si - li < len(nums) - si - 1:
                    sum += si - li
                else:
                    sum += len(nums) - si
            else:
                sum = len(nums) - si
                if li < si - li - 1:
                    sum += li + 1
                else:
                    sum += si - li
        return sum
