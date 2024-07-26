class Solution:
    def memLeak(self, mem1: int, mem2: int) -> List[int]:
        i = 1
        while True:
            if mem1 >= mem2:
                if mem1 < i:
                    break
                mem1 -= i
            else:
                if mem2 < i:
                    break
                mem2 -= i
            i += 1
        return [i, mem1, mem2]   