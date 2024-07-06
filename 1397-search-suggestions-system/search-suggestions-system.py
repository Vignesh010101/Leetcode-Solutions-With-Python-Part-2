class Solution:
    def suggestedProducts(self, p: List[str], s: str) -> List[List[str]]:
        p.sort()
        ret = []
        for i in range(1, len(s) + 1):
            j=bisect_left(p, s[:i])
            ret.append([x for x in p[j:j+3] if x.startswith(s[:i])])
        return ret  