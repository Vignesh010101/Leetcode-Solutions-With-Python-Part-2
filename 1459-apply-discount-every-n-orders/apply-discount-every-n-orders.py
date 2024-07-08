class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.cur = 0
        self.discount = discount
        self.lookup = defaultdict(int)
        for u, v in zip(products, prices):
            self.lookup[u] = v

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for u, v in zip(product, amount):
            total += self.lookup[u] * v
        
        self.cur += 1
        if self.cur == self.n:
            self.cur = 0
            total *= (100 - self.discount) / 100

        return total
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)