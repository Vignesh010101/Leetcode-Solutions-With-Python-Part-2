class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = [[reward1[i] - reward2[i], i] for i in range(len(reward1))]
        diff.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += reward1[diff[i][1]]
        for i in range(k, len(reward1)):
            ans += reward2[diff[i][1]]
        return ans