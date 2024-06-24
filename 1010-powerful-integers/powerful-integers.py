class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound <= 1: return []
        
        res = set()
        L = int(log(bound, x)) + 1 if x > 1 else 1
        M = int(log(bound, y)) + 1 if y > 1 else 1

        for i in range(L):
            for j in range(M):
                s = x**i + y**j
                if s <= bound:
                    res.add(s)

        return list(res)