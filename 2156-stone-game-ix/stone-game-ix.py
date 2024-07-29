class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        freq = defaultdict(int)
        for x in stones: freq[x % 3] += 1
        
        if freq[0]%2 == 0: return freq[1] and freq[2]
        return abs(freq[1] - freq[2]) >= 3