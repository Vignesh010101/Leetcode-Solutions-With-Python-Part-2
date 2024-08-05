class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:        
        if num == 0:
            return 0
        
        target_last_digit = num % 10
        cur_sum = k
        min_size = 1
        visited = set()
        
        while cur_sum <= num:
            cur_last_digit = cur_sum % 10
            if cur_last_digit == target_last_digit:
                return min_size
            
            else:
                if cur_last_digit in visited:
                    return -1
                
                visited.add(cur_last_digit)
            
            cur_sum += k
            min_size += 1
        
        return -1