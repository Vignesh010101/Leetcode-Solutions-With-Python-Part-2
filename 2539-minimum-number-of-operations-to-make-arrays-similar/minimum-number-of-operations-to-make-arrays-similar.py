from sortedcontainers import SortedList
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        odd_nums = SortedList([num for num in nums if num % 2 == 1])
        even_nums = SortedList([num for num in nums if num % 2 == 0])
        odd_target = SortedList([num for num in target if num % 2 == 1])
        even_target = SortedList([num for num in target if num % 2 == 0])
        ans = 0
        while odd_nums:
            ans += abs(odd_nums[0] - odd_target[0]) // 2
            odd_nums.pop(0)
            odd_target.remove(odd_target[0])
        while even_nums:
            ans += abs(even_nums[0] - even_target[0]) // 2
            even_nums.pop(0)
            even_target.remove(even_target[0])
        return ans // 2