from collections import defaultdict
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        d = defaultdict(list)
        for word in words:
            odd , even = "",''
            for idx,char in enumerate(word):
                if idx%2 == 0:
                    even += char
                else:
                    odd+= char

            odd = sorted(odd)
            even = sorted(even)
            final = "".join(odd+even)
            
            d[final].append(word)

        
        return len(d.values())