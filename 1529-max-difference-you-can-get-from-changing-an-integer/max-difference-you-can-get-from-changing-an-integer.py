class Solution:
    def maxDiff(self, num: int) -> int:
        numList = list(str(num))
        greaterNumber, smallerNumber = str(num), str(num)
        numToReplace = -1
        for char in greaterNumber:
            if int(char) < 9:
                numToReplace = char
                break
        if numToReplace != -1:
            for i,val in enumerate(numList):
                if val == numToReplace:
                    numList[i] = '9'
            
            greaterNumber = int(''.join(numList))
        
        numList = list(str(num))
        numToReplace = -1
        for char in smallerNumber:
            if int(char) > 1:
                numToReplace = char
                break
        if numToReplace != -1:
            newreplacement = '1'
            if smallerNumber[0] != numToReplace:
                newreplacement = '0'
            for i,val in enumerate(numList):
                if val == numToReplace:
                    numList[i] = newreplacement
            
            smallerNumber = int(''.join(numList))
        
        return int(greaterNumber) - int(smallerNumber)


        