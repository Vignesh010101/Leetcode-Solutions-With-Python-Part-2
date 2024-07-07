class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def exchange(numBottles,numExchange):
            if numBottles<numExchange:
                return 0
            no, remaining=divmod(numBottles, numExchange)
            return no+exchange(no+remaining,numExchange)
        return numBottles+exchange(numBottles,numExchange)