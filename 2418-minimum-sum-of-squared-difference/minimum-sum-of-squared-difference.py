class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        dif = [abs(nums2[i] - nums1[i]) for i in range(len(nums2))]
        dif.sort(reverse=True)
        dif.append(0)
        pre = 0
        index = -1
        for i in range(1, len(dif)):
            after = pre + (dif[i - 1] - dif[i]) * i
            if after > k1 + k2:
                index = i
                break
            pre = after
        if index == -1:
            return 0
        excess = k1 + k2 - pre
        if index > 0:
            mod = excess % index
        else:
            mod = 0
        for i in range(mod):
            dif[i] = dif[index - 1] - (excess + index - 1) // index
        for i in range(mod, index):
            dif[i] = dif[index - 1] - excess // index

        out = 0
        for i in range(len(dif)):
            out += dif[i]**2
        return out