class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        ans = prefix = 0 
        health = [ceil(h/power) for h in health]
        for d, h in sorted(zip(damage, health), key = lambda x: -x[0]/x[1]): 
            prefix += h 
            ans += d*prefix 
        return ans 