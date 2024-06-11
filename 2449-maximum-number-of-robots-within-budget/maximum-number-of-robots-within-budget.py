class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        queue = deque()
        left = best_length = curr = 0

        for right in range(len(chargeTimes)):
        	curr += runningCosts[right]
        	while queue and chargeTimes[queue[-1]] < chargeTimes[right]:
        		queue.pop()

        	queue.append(right)

        	while queue and (chargeTimes[queue[0]] + (right - left + 1) * curr) > budget:
        		if queue[0] == left:
        			queue.popleft()
        		curr -= runningCosts[left]
        		left += 1

        	best_length = max(best_length, right - left + 1)

        return best_length