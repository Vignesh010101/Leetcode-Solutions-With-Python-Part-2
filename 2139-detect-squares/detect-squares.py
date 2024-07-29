class DetectSquares:

    def __init__(self):
        self.freq = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.freq[point] = 1 + self.freq.get(point, 0)

    def count(self, point: List[int]) -> int:
        ans = 0 
        x, y = point
        for xx, yy in self.freq: 
            if xx != x and abs(x-xx) == abs(y-yy): 
                ans += self.freq[xx, yy] * self.freq.get((xx, y), 0) * self.freq.get((x, yy), 0)
        return ans 

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)