class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        st1 = [] # monotonic decreasing first stack.
        st2 = [] # Monotonic decreasing second stack.(having only that elements which have first greater)
        helper = [] # monotonic increasing helper stack(help in moving elements from st1 to st2 with maintaining monotonicity of st2) 
        n = len(nums)
        ans =[-1]*n
        for i in range(n):
            while st2 and nums[i]>nums[st2[-1]]: # if element can be second largest for st2 elements
                ans[st2.pop()] = nums[i]
            while st1 and nums[i]>nums[st1[-1]]: # if element can be second largest for st2 elements
                helper.append(st1.pop())
            while helper:
                st2.append(helper.pop())    # for maintain monotonicity of st2
            st1.append(i)
        return ans   