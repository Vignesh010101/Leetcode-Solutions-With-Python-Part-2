class ATM:

    def __init__(self):
        self.den = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}
    
    def deposit(self, banknotesCount: List[int]) -> None:
        for i ,j in [(0,20),(1,50),(2,100),(3,200),(4,500)]:
            self.den[j] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0, 0, 0, 0, 0]
        for i ,j in ((0,500),(1,200),(2,100),(3,50),(4,20)):
            if amount >= j:
                ans[4-i] = min(self.den[j],amount//j)
                amount -= ans[4-i] * j
        if amount: return [-1]
        for i,j in [(0,20),(1,50),(2,100),(3,200),(4,500)]:
            self.den[j] -= ans[i]
        return ans

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)