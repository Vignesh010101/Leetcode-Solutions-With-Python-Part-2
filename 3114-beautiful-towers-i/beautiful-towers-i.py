class Solution:
    def getMinSubtract(self, A, n):
        ans = [0]*n
        st = [(A[0], 1)]
        for i in range(1, n):
            ans[i] = ans[i-1]
            newWidth = 1
            while st and A[i] < st[-1][0]:
                height, width = st.pop()
                ans[i] += (height - A[i]) * width
                newWidth += width
            st.append((A[i], newWidth)) 
        return ans

    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        minSubtract = sum(maxHeights)
        left = self.getMinSubtract(maxHeights, n)
        right = self.getMinSubtract(maxHeights[::-1], n)[::-1]
        for i in range(n):
            minSubtract = min(minSubtract, left[i] + right[i])
        return sum(maxHeights) - minSubtract