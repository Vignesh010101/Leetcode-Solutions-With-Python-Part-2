class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        
        def not_less_than_median(x: int, cnt = 0, left = -1)-> bool:

            d = defaultdict(int)
            
            for rght in range(n):
                d[nums[rght]]+= 1

                while len(d) > x:
                    left+= 1
                    d[nums[left]] -= 1
                    if d[nums[left]] == 0: del d[nums[left]]

                cnt+= rght - left
                if cnt >= median: return True

            return False
        

        n = len(nums)
        median = (comb(n+1,2) + 1) // 2
        return bisect_left(range(n), 
                            True, key = not_less_than_median)