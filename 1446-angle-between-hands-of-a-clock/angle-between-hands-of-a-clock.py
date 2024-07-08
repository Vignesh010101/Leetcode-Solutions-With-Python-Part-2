class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        poss = [abs((((hour * 5) + (5 * (minutes / 60))) * 6) - minutes * 6), abs((360 - (((hour * 5) + (5 * (minutes / 60))) * 6)) + (360 - minutes * 6)), abs(((((hour * 5) + (5 * (minutes / 60))) * 6)) + (360 - minutes * 6)), abs((360 - (((hour * 5) + (5 * (minutes / 60))) * 6)) + (minutes * 6))]
        return min(poss)