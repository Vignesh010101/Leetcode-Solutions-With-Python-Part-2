class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs = sorted(logs, key = itemgetter(1))
        queries = sorted((query, i) for i, query in enumerate(queries))
        cnt_serv = defaultdict(int)
        left, right, m = 0, 0, len(logs)
        ans = [0]*len(queries)
        for end, i in queries:
            start = end - x
            while right < m and logs[right][1] <= end:
                cnt_serv[logs[right][0]] += 1
                right += 1
            while left < right and logs[left][1] < start:
                cnt_serv[logs[left][0]] -= 1
                if not cnt_serv[logs[left][0]]:
                    del cnt_serv[logs[left][0]]
                left += 1
            ans[i] = n - len(cnt_serv)
        return ans   