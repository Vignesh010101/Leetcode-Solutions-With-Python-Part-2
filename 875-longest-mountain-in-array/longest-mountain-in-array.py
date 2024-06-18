class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        up = 0
        down = 0

        for i in range(1, len(arr)):
            if (down and arr[i - 1] < arr[i]) or (arr[i - 1] == arr[i]):
                up = 0
                down = 0

            up += arr[i - 1] < arr[i]
            down += arr[i - 1] > arr[i]

            if up and down:
                longest = max(longest, up + down + 1)

        return longest  
        