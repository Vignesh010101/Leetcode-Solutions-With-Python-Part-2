class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        n = len(arr)
        s = 1
        ans1 = 1
        start = [arr[0]]
        while s < n and arr[s-1] <= arr[s]:
            ans1 += 1
            start.append(arr[s])
            s += 1
        if start == arr:
            return 0
        
        e = n-2
        ans2 = 1
        end = [arr[n-1]]
        while e > 0 and arr[e] <= arr[e+1]:
            ans2 += 1
            end.append(arr[e])
            e -= 1
        
        ans = max(ans1, ans2)

        m = len(end)
        for j in range(m-1, -1, -1):
            ans = max(ans, bisect.bisect_right(start, end[j]) + j + 1)
        
        return n-ans