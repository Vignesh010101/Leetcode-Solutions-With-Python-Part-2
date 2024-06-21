class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        frequency = Counter(s)
        uniqueChars = list(frequency.keys())

        @cache
        #return (maxBeauty, count of maxBeauty sequences)
        def dp(charIndex, k): 
            if k == 0:
                return 0, 1
            if k > charIndex + 1: #k is greater than the number of remaining unique characters
                return 0, 0

            #not take the current character
            beauty, count = dp(charIndex - 1, k)

            #take the current character
            charFre = frequency[uniqueChars[charIndex]]
            subBeauty, subCount = dp(charIndex - 1, k - 1)
            beautyIfTake, countIfTake = subBeauty + charFre, subCount * charFre
            if beautyIfTake > beauty:
                beauty, count = beautyIfTake, countIfTake
            elif beautyIfTake == beauty:
                count += countIfTake
            
            return beauty, count % MOD 

        
        return dp(len(uniqueChars) - 1, k)[1]