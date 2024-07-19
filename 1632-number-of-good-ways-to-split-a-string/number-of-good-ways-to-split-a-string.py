class Solution:
    def numSplits(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 0
        elif length == 2:
            return 1
		
        first = {} 
        last = {}  
		
        for index, character in enumerate(s):  
            if character not in first:
                first[character] = index
            last[character] = index
        indices = list(first.values()) + list(last.values())  
        indices.sort()
        middle = len(indices)//2 
        return indices[middle] - indices[middle-1]