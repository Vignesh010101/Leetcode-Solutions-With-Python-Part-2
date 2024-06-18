class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # L*G = p*q  <=> L/q = p/G <=> L/p = q/G

        G = gcd(p,q)
        p//= G
        q//= G
        
        return 2 if p%2 == 0 else q%2