class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [0] + spaces + [len(s)]
        ans = []
        for i in range(1, len((spaces))):
            ans.append(s[spaces[i-1]:spaces[i]])
        return " ".join(ans)

        