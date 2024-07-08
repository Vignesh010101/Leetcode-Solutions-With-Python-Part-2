class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events = sorted(events)
        minhpq = []                
        today = 0                
        i = 0                      
        count = 0
        
        while minhpq or i < n:
            if not minhpq:
                today = events[i][0]
            while i < n and events[i][0] == today:
                end = events[i][1]
                heappush(minhpq, end)
                i += 1
            heappop(minhpq)
            count += 1
            today += 1  
            while minhpq and minhpq[0] < today:
                heappop(minhpq)

        return count