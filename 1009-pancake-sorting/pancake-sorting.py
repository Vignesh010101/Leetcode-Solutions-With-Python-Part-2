class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr), 1, -1):
            max_idx = arr.index(i)
            res.extend([max_idx + 1, i])
            first = arr[:max_idx+1][::-1]
            arr = first + arr[max_idx+1:]
            second = arr[:i][::-1]
            arr = second + arr[i:]
        return res