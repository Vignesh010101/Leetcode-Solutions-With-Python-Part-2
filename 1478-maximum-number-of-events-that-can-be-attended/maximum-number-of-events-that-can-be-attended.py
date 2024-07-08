class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events = sorted(events)    # sort based on the start day
        minhpq = []                # min heap to store finishing time of events ascendingly 
        today = 0                  # pointer for current day
        i = 0                      # pointer for events
        count = 0
        
        while minhpq or i < n:
            # if empty, then set today to start time of event[i]
            if not minhpq:
                today = events[i][0]

            # 1. add the end time of every task with the same starting day as of today
            while i < n and events[i][0] == today:
                end = events[i][1]
                heappush(minhpq, end)
                i += 1

            # 2. greedily finish the task with earliest time
            heappop(minhpq)
            count += 1

            # next valid day
            today += 1  

            # 3. clean up; remove any task finishes before valid today pointer
            while minhpq and minhpq[0] < today:
                heappop(minhpq)

        return count