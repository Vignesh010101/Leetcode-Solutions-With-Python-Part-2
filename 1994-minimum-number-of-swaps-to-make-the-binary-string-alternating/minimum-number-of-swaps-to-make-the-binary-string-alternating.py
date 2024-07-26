class Solution:
    def minSwaps(self, s: str) -> int:
        ones = s.count("1")
        zeros = len(s) - ones 
        if abs(ones - zeros) > 1: return -1 # impossible
        
        def fn(x):
            ans = 0 
            for c in s: 
                if c != x: ans += 1
                x = "1" if x == "0" else "0"
            return ans//2
        
        if ones > zeros: return fn("1")
        elif ones < zeros: return fn("0")
        else: return min(fn("0"), fn("1")) 