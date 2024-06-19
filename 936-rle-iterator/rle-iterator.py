class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.qrle = deque()
        n = len(encoding)
        for i in range(0, n, 2):
            count, elem = encoding[i], encoding[i+1]
            if count:
                self.qrle.append((count, elem))    

    def next(self, n: int) -> int:
        last_elem = 0
        while n:
            if not self.qrle:
                last_elem = -1
                break
                
            count, elem = self.qrle.popleft()
            if count >= n:
                last_elem = elem
                if count > n: self.qrle.appendleft((count-n, elem))
                break
            else:
                n -= count
        
        return last_elem


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

