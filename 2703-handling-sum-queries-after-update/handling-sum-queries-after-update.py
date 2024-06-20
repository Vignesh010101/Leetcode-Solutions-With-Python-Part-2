class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # get nums1 as the binary representation of some number
        n1 = int(''.join([str(d) for d in nums1]), 2)
        res = []
        key = False
        # calculate sum of nums1 and nums2
        sum1, sum2 = n1.bit_count(), sum(nums2)
        for t, left, right in queries:
            if t == 1:
                # make xor of nums1 to flip corresponding bits
                temp = '1'*(right - left + 1) + '0'*(len(nums1) - right - 1)
                n1 ^= int(temp, 2)
                key = True
            if t == 2:
                # we don't recalculate sum1 when it isn't necessary
                if key:
                    sum1 = n1.bit_count()
                    key = False

                sum2 += left*sum1      
            if t == 3:
                res.append(sum2)
        
        return res                   