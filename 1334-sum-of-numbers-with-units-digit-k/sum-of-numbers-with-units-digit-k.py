class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            if num % 10 == 0:
                return 1
            else:
                return -1
        cycles = {1:[0,1,2,3,4,5,6,7,8,9], 2:[0, 2,4,6,8], 3:[0, 3,6,9,2,5,8,1,4,7], 4:[0, 4,8,2,6], 5:[0,5],6:[0,6,2,8,4],7:[0,7,4,1,8,5,2,9,6,3],8:[0,8,6,4,2],9:[0,9,8,7,6,5,4,3,2,1]}
        l_digit = num % 10
        if l_digit not in cycles[k]:
            return -1
        ind = cycles[k].index(l_digit)
        if ind == 0:
            ind = len(cycles[k])
        if num < k * ind:
            return -1
        return ind
        
        

        