class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        pref = [0] + pref
        return [pref[i] ^ pref[i-1] for i in range(1, len(pref))]