class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        currLen = 0
        currSum = 0
        ans = 0

        for i in range(0, len(arr)):

            if currLen == k:

                if currSum >= threshold:
                    ans += 1

                currSum = currSum - (arr[i-k]/k)
                currLen -= 1

            currSum += (arr[i]/k)
            currLen += 1

        if currSum >= threshold:
            ans += 1
            
        return ans
