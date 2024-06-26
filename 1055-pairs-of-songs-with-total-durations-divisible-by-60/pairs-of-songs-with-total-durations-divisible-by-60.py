class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        reverseMap = {}
        count = 0
        sixtyCount = 0
        
        for song in time:
            index = 60 - song % 60

            if(song % 60 == 0):
                sixtyCount += 1
                continue
                
            if(song % 60 in reverseMap):
                count += reverseMap[song % 60]
            
            if(index in reverseMap):
                reverseMap[index] += 1
            else:
                reverseMap[index] = 1
        
        # n choose 2 where n = # songs perfectly divisible by 60
        return count + comb(sixtyCount, 2)