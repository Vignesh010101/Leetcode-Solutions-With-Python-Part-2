class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        mx, stack, res, prev, num = nums[0], [], 0, nums[0], nums[1]
        for next in nums[2:]:
            if prev < num < next:
                res += 1
            if num > mx:
                mx = num
                stack.append(num)
            else:
                while stack and stack[-1] >= num:   stack.pop()
            prev, num = num, next
        while stack and stack[-1] >= num:  stack.pop()
        return res + len(stack)