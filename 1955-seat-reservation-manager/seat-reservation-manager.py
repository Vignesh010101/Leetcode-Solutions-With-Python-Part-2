class SeatManager:

    def __init__(self, n):
        self.pq = list(range(1, n + 1))
        heapq.heapify(self.pq)

    def reserve(self):
        val = heapq.heappop(self.pq)
        return val

    def unreserve(self, seatNumber):
        heapq.heappush(self.pq, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)