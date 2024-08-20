class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        total_piles = len(piles)
        suffix_sums = [0] * (total_piles + 1)
        for i in range(total_piles - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
        
        memo = [[0] * (total_piles + 1) for _ in range(total_piles)]
        
        def max_stones_alice_can_get(m: int, current_pile: int) -> int:
            if current_pile >= total_piles:
                return 0
            
            if current_pile + 2 * m >= total_piles:
                return suffix_sums[current_pile]
            
            if memo[current_pile][m] != 0:
                return memo[current_pile][m]
            
            max_stones = 0
            
            for x in range(1, 2 * m + 1):
                current_stones = suffix_sums[current_pile] - max_stones_alice_can_get(max(m, x), current_pile + x)
                max_stones = max(max_stones, current_stones)
            
            memo[current_pile][m] = max_stones
            return max_stones
        
        return max_stones_alice_can_get(1, 0)