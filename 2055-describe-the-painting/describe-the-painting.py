class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        mapping = defaultdict(int)
        for s, e, c in segments:
            mapping[s] += c
            mapping[e] -= c
        
        res = []
        prev, color = None, 0
        for now in sorted(mapping):
            if color: 
                res.append((prev, now, color))
            
            color += mapping[now]
            prev = now
            
        return res