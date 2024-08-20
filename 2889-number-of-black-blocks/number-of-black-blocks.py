class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        mp = {}
        for v in coordinates:
            if v[0] > 0:
                mp[(v[0] - 1, v[1])] = mp.get((v[0] - 1, v[1]), 0) + 1
            if v[1] > 0:
                mp[(v[0], v[1] - 1)] = mp.get((v[0], v[1] - 1), 0) + 1
            if v[0] > 0 and v[1] > 0:
                mp[(v[0] - 1, v[1] - 1)] = mp.get((v[0] - 1, v[1] - 1), 0) + 1
            mp[(v[0], v[1])] = mp.get((v[0], v[1]), 0) + 1
        
        answer = [0] * 5
        nonzeros = 0
        for kv in mp.items():
            black = kv[1]
            if kv[0][0] != m - 1 and kv[0][1] != n - 1:
                answer[black] += 1
                nonzeros += 1
        answer[0] = (m - 1) * (n - 1) - nonzeros
        return answer