class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        ans = 0
        diff = {}
        
        reward = [0] * len(reward1)
        
        for i in range(len(reward1)):
            diff[i] = reward1[i] - reward2[i]
            
        sortDiff = sorted(diff.items(), key = lambda x:x[1], reverse = True)
        
        for i in range(k):
            index = sortDiff[i][0]
            ans += reward1[index]
        
        for i in range(len(reward1) - k):
            index = sortDiff[i + k][0]
            ans += reward2[index]
        
        return ans 