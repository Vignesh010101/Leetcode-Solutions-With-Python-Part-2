class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if k == 1: return "a"
        b = int(log2(k-1))
        ans = self.kthCharacter(k-2**b, operations)
        if operations[b] == 1: ans = chr((ord(ans)-96)%26 + 97)
        return ans