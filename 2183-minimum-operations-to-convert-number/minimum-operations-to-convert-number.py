class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        n = len(nums)
        que = [start]
        steps = 0
        visited = set()
        while que:
            # print(que)
            nxt = []
            for x in que:
                if x == goal:
                    return steps
                if x in visited or x < 0 or x > 1000:
                    continue
                visited.add(x)
                for i in range(n):
                    nxt.append(x + nums[i]) 
                    nxt.append(x - nums[i])
                    nxt.append(x ^ nums[i]) 
            steps += 1
            que = nxt
        return -1