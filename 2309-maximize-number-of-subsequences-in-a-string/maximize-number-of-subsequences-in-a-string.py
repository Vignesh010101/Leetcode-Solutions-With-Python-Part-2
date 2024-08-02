class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
        a = pattern[0]
        b = pattern[1]
        if a==b:
            count = 1
            for e in text:
                if e == a:
                    count += 1
                
            return int(count*(count-1)/2)
        count_a = 0
        count_b = 0
        total_count = [0,0]
        for e in text:
            if e == a:
                count_a += 1
            elif e == b:
                count_b += 1
                total_count[0] += count_a
                total_count[1] += count_a+1
        
        return max(total_count[0]+count_a, total_count[1])