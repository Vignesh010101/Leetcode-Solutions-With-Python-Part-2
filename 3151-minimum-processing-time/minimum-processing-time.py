class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        ans,ind=0,0
        for i in range(len(processorTime)):
            ans=max(ans,processorTime[i]+tasks[ind])
            ind+=4
        return ans