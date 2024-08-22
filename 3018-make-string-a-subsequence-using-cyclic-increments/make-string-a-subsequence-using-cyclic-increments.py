d = dict(pairwise(ascii_lowercase+'a'))

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        n1, n2 = len(str1), len(str2)
        i1 = i2 = 0

        while i1 < n1 and i2 < n2:
            if str1[i1] == str2[i2] or d[str1[i1]] == str2[i2]: i2+= 1
            i1 += 1

        return i2 == n2