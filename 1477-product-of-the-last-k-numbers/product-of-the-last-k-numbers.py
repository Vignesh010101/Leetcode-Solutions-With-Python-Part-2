
class ProductOfNumbers:

    def __init__(self):
        self.queue=deque()
        self.count_of_one = 0

    def add(self, num: int) -> None:
        self.queue.append(num)
        if(num == 1):
            self.count_of_one += 1

    def getProduct(self, k: int) -> int:
        if(self.count_of_one == len(self.queue)):
            return 1
        else:
            t =1
            ls= []
            while(k>0):
                q = self.queue.pop()
                t*=q
                ls.append(q)
                k-=1
            ls = ls[::-1]
            for i in ls:
                self.queue.append(i)
            return t
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)