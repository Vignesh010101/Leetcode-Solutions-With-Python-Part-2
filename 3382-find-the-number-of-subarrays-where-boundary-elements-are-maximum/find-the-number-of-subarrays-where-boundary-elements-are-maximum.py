class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        st = deque()
        ans = 0
        for x in nums:
            while st and st[-1][0] < x:
                st.pop()
            if not st or st[-1][0] != x:
                st.append((x, 1))
            else:
                st[-1] = (st[-1][0], st[-1][1] + 1)
            ans += st[-1][1]
        return ans