class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        index = 0
        l = len(passengers)
        for start in buses:
            cap = capacity
            while index < len(passengers) and start >= passengers[index] and cap > 0:
                cap -= 1
                index += 1

        latest = start if cap > 0 else passengers[index-1] 

        while latest in set(passengers):
            latest -= 1
        return latest            
            
                                    