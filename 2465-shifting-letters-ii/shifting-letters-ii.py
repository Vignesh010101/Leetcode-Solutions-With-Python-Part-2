class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        offsets = [0]*(n+1)                                     
		
        for start, end, direction in shifts:                    
            offsets[start]+= 2*direction-1
            offsets[end+1]-= 2*direction-1
			
        offsets = accumulate(offsets)                          

        chNums = (ord(ch)-97 for ch in s)                       
		
        chNums = ((chNum + offset)%26 for chNum,               
                   offset in zip(chNums, offsets))

        return ''.join(chr(chNum+97) for chNum in chNums)       