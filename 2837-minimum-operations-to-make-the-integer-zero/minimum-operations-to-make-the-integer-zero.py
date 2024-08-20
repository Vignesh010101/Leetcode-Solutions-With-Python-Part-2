class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 <= num2:
            return -1
            
        moves = 0
        while True:
            if num1 - num2 < moves + 1:
                return -1
            num1 -= num2
            moves += 1
            if bin(num1)[2:].count('1') <= moves:
                break

        return moves