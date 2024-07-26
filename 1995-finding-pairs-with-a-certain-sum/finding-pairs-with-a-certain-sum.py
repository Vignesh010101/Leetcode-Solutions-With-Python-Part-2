class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.freqs1 = Counter(nums1)
        self.freqs2 = Counter(nums2)
        self.nums2 = nums2[:]
        
    def add(self, index: int, val: int) -> None:
        if not val: return

        n = self.nums2[index]
        f = self.freqs2[n]
        if f == 1:
            del self.freqs2[n]
        else:
            self.freqs2[n] -= 1

        self.nums2[index] += val
        self.freqs2[n+val] = self.freqs2.get(n+val, 0) + 1

    def count(self, tot: int) -> int:
        if len(self.freqs1) <= len(self.freqs2):
            fs1, fs2 = self.freqs1, self.freqs2
        else:
            fs1, fs2 = self.freqs2, self.freqs1

        ans = 0
        for n1, f1 in fs1.items():
            if n1 >= tot: continue

            ans += f1*fs2.get(tot-n1, 0)

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)