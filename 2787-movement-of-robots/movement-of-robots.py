class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:

        nums = sorted([num+(ord(ch)-79)//3*d            # Example : nums: [1,0,4,-5],  s:  'RLRL',  d:  2
                       for num, ch in zip(nums,s)])    
                                                        #  nums = sorted([1+2, 0-2, 4+2, -5-2])
                                                        #       = [-7,-2,3,6]

        return sum(map(mul, nums, range(1-len(nums),    #  sum(map(mul, [[-7,-2,3,6],[-3,-1,1,3]]))
                       len(nums), 2)))%1000000007       #  sum((-7*-3)+(-2*-1)+(3*1)+(6*3))
                                                        #  return 44