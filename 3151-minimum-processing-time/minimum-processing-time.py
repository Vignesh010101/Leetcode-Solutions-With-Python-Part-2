class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        min_time = counter = 0

        for x in range(3, len(tasks), 4):
            min_time = max(processorTime[counter] + tasks[x], min_time)
    
            counter += 1

        return min_time