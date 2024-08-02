class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = list(set(nums)) 
        nums.sort()  
        last_term = k
        removable_sum = 0
        for num in nums :
            if (num <= last_term) : 
                last_term += 1 
                removable_sum += num  
            else :
                break  
        somme = (last_term * (1 + last_term) / 2) - removable_sum
        return int(somme)