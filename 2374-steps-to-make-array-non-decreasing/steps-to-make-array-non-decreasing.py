class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = [(nums[-1], 0)]
        n = len(nums)
        max_step = 0
        for i in range(n - 2, -1, -1):
            num = nums[i]
            if num <= stack[-1][0]:
                stack.append((num, 0))
                continue
            step = 0
            while stack and num > stack[-1][0]:
                step += 1
                _, old_step = stack.pop()
                if old_step > step:
                    step = old_step
            if step > max_step:
                max_step = step
            if stack and stack[-1][1] < step + 1:
                stack[-1] = (stack[-1][0], step + 1) 
            stack.append((num, 0))

        return max_step 