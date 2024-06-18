class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        runningSum = 0
        charList = list(s)

        for i in range(len(charList)-1,-1,-1):
            runningSum += shifts[i]
            runningSum %= 26
            shifted_val = (ord(charList[i]) - ord('a') + runningSum) % 26
            charList[i] = chr(ord('a') + shifted_val)
        return ''.join(charList)