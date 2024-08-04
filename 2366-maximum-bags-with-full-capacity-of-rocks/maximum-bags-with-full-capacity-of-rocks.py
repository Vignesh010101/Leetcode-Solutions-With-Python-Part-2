class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        rock = [capacity[x] - rocks[x] for x in range(len(capacity))]
        bags = rock.count(0)
        rock = [x for x in rock if x != 0]
        rock.sort()

        for x in rock:
            if not additionalRocks - x < 0:
                bags += 1
                additionalRocks -= x
            else:
                break

        return bags