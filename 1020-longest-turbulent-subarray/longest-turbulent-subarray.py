class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        max_size = 1

        last = arr[0]

        curr_size = 1
        
        last_op = 0 # 0 == eq, 1 == gt, 2 == lt

        for n in arr[1:]:
            if n > last:
                if last_op != 2:
                    curr_size = 2
                else:
                    curr_size += 1
                last_op = 1
            elif n < last:
                if last_op != 1:
                    curr_size = 2
                else:
                    curr_size += 1
                last_op = 2
            else:
                curr_size = 1
                last_op = 0
                      
            last = n

            if curr_size > max_size:
                max_size = curr_size

        return max_size