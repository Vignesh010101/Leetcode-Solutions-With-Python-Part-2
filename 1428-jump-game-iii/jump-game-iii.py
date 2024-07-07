class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q, n, i = deque([start]), len(arr), start

        while q and arr[i] != 0:
            i = q.popleft()
            left_index, right_index = i-arr[i], i+arr[i]
            if left_index > -1 and arr[left_index] > -1:
                q.append(left_index)
            if right_index < n and arr[right_index] > -1:
                q.append(right_index)
            arr[i] *= -1

        return arr[i] == 0