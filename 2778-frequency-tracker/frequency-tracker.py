from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.ds = defaultdict(int)
        self.fs = defaultdict(int)

    def add(self, number: int) -> None:
        self.fs[self.ds[number]] -= 1
        self.ds[number] += 1
        self.fs[self.ds[number]] += 1

    def deleteOne(self, number: int) -> None:
        self.fs[self.ds[number]] -= 1
        self.ds[number] = max(0,self.ds[number] - 1)
        self.fs[self.ds[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.fs[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)