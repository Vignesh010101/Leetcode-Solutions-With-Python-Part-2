class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], n: int, use_limit: int) -> int:
        labels_cnt = Counter()
        vals = [(-v, l) for v, l in zip(values, labels)]
        vals.sort()

        values = []
        for v, l in vals:
            if labels_cnt[l] >= use_limit:
                continue
            values.append(v)
            labels_cnt[l] += 1

        heapq.heapify(values) 
        return -sum(heapq.heappop(values) for _ in range(min(n, len(values))))