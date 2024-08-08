class Solution:
    # Function to count the number of set bits (1s) in a number
    def countSetBits(self, number):
        count = 0
        while number != 0:
            count += (number & 1)
            number = number >> 1
        return count

    # Function to set the least significant unset bits in 'number' 
    def addSetBits(self, number, bitsToAdd):
        bitPosition = 0
        while bitsToAdd > 0:
            while (number >> bitPosition) & 1 == 1:
                bitPosition += 1
            number = number | (1 << bitPosition)
            bitsToAdd -= 1
        return number

    # Function to remove the least significant set bits in 'number'
    def removeSetBits(self, number, bitsToRemove):
        while bitsToRemove > 0:
            number = number & (number - 1)
            bitsToRemove -= 1
        return number

    def minimizeXor(self, num1, num2):
        setBitsNum1 = self.countSetBits(num1)
        setBitsNum2 = self.countSetBits(num2)

        # If num1 already has the same number of set bits as num2
        if setBitsNum1 == setBitsNum2:
            return num1

        # If num1 has fewer set bits than num2, add the necessary set bits
        if setBitsNum1 < setBitsNum2:
            return self.addSetBits(num1, setBitsNum2 - setBitsNum1)

        # If num1 has more set bits than num2, remove the extra set bits
        return self.removeSetBits(num1, setBitsNum1 - setBitsNum2)