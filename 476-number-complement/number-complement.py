class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)[2:]
        flip=''.join(['0' if bt=='1' else '1' for bt in binary])
        if flip:
            return int(flip,2)
        else:
            return 1