class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0

        for num in nums: 
            if num%2 == 0: total += num
        answer = []

        for i in range(len(queries)):
            num = queries[i][0]
            idx = queries[i][1]
            idx_sum = nums[idx] + num
            if not (nums[idx] % 2 != 0 and idx_sum % 2!= 0):
                if idx_sum % 2 == 0:
                    if nums[idx] % 2 != 0: total = total + idx_sum
                    else: total = total + num
                else: total = total - nums[idx]
            
            nums[idx] = idx_sum
            answer.append(total)
        
        return answer