class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        first_ele = 0
        for i in range(1, len(encoded)+2):
            first_ele = first_ele^i
        for i in range(1, len(encoded), 2):
            first_ele = first_ele^encoded[i]
        ans = [first_ele]
        for i in encoded:
            z = ans[-1]^i
            ans.append(z)
        return ans