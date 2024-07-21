class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        customerswaiting = 0
        customersriding = 0
        profit = []
        i = 0
        while customerswaiting>0 or i<len(customers):
            if i < len(customers):
                customerswaiting += customers[i]
            if customerswaiting>3:
                customersriding += 4
                customerswaiting -= 4
            else:
                customersriding += customerswaiting
                customerswaiting = 0
            i += 1
            x = customersriding*boardingCost - i*runningCost
            if len(profit) == 0:
                maxp = x
            else:
                maxp = max(maxp, x)
            profit.append(x)
        if maxp <= 0:
            return -1
        return profit.index(maxp)+1