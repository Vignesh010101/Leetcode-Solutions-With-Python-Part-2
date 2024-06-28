class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        def gen():
            nonlocal label
            lv, q = 0, label
            yield label
            while q:
                q, r = divmod(q, 2)
                lv += (q > 0)
            real_parent = label
            for i in range(lv - 1, -1, -1):
                original_parernt = label // 2
                offset = abs(original_parernt - 2 ** (i + 1)) - 1
                real_parent = 2 ** i + offset
                yield real_parent
                label = real_parent

        return list(gen())[::-1]