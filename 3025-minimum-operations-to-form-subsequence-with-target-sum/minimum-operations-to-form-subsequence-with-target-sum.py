class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        target = bin(target)[2:]
        nums = [int(math.log2(x)) for x in nums]
        ct = Counter(nums)
        step,exp,cur_sum = 0,0,0
        for i in target[::-1]:
            ct_keys = sorted(list(ct.keys()))
            if i == '1':
                if exp in ct:
                    ct[exp] -= 1
                    if ct[exp] == 0:
                        del ct[exp]
                elif cur_sum >= 2**exp:
                    cur_sum -= 2**exp
                else:
                    index = bisect_left(ct_keys,exp)
                    if index == len(ct_keys):
                        return -1
                    else:
                        index = ct_keys[index]
                        while index != exp:
                            ct[index]-=1
                            if ct[index] == 0:
                                del ct[index]
                            index-=1
                            ct[index]+=2
                            step+=1
                        ct[index] -= 1
            cur_sum+=ct[exp]*2**(exp)
            exp+=1
        return step
        