class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        lst_n = list(map(int, str(n)))
        lst_n.reverse()
        ans = []
        i = 0
        while sum(lst_n) > target:
            if lst_n[i] > 0:
                diff = 10 - lst_n[i]
                ans.append(diff)
                lst_n[i] = 0
                if i + 1 < len(lst_n):
                    lst_n[i + 1] += 1
                else:
                    lst_n.append(1)
            else:
                ans.append(0)
            i += 1
        if ans:
            return sum(v * pow(10, i) for i, v in enumerate(ans))
        return 0