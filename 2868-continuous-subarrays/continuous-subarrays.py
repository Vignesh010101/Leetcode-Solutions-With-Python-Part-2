class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        min_stack = deque()
        max_stack = deque()
        left = 0
        n = len(nums)
        answer = 0

        for right in range(n):
            
            while max_stack and max_stack[-1] < nums[right]:
                max_stack.pop()

            while min_stack and min_stack[-1] > nums[right]:
                min_stack.pop()
            
            max_stack.append(nums[right])
            min_stack.append(nums[right])

            while max_stack[0] - min_stack[0] > 2:

                if nums[left] == max_stack[0]:
                    max_stack.popleft()
                
                if nums[left] == min_stack[0]:
                    min_stack.popleft()
                
                left += 1
            
            #print(right,left,right-left+1)
            answer += (right-left+1)
        
        return answer

        