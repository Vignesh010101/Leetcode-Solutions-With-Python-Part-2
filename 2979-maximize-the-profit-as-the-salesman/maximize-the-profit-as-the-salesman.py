class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        mp = {}
        for i in offers:
            if i[0] not in mp:
                mp[i[0]] = []
            mp[i[0]].append([i[1], i[2]])
        
        arr = [0] * n
        prof = 0
        
        for i in range(n):
            if i in mp:
                for j in mp[i]:
                    arr[j[0]] = max(arr[j[0]], j[1] + prof)
            prof = max(prof, arr[i])
        
        return prof
        