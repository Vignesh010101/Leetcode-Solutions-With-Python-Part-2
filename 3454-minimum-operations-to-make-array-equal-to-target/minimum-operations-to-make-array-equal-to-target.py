class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        x = 0
        vec = [target[i] - nums[i] for i in range(len(nums))]
        n = len(vec)
        last = vec[0]

        if n == 1:
            return abs(last)
        elif n == 2:
            if (vec[0] >= 0 and vec[1] >= 0) or (vec[0] < 0 and vec[1] < 0):
                return max(abs(vec[0]), abs(vec[1]))
            else:
                return abs(vec[0]) + abs(vec[1])
        else:
            x += abs(last)
            f = last >= 0
            for i in range(1, n - 1):
                if f:
                    if vec[i] == last:
                        continue
                    if last < vec[i] and vec[i] > vec[i + 1]:
                        x += abs(vec[i] - last)
                        last = vec[i]
                        f = last >= 0
                    elif last > vec[i] and vec[i] < vec[i + 1]:
                        if vec[i] < 0:
                            x += abs(vec[i])
                        last = vec[i]
                        f = last >= 0
                else:
                    if vec[i] == last:
                        continue
                    if last < vec[i] and vec[i] > vec[i + 1]:
                        if vec[i] > 0:
                            x += abs(vec[i])
                        last = vec[i]
                        f = last >= 0
                    elif last > vec[i] and vec[i] < vec[i + 1]:
                        x += abs(vec[i] - last)
                        last = vec[i]
                        f = last >= 0

            if last >= 0 and vec[n - 1] > 0 and vec[n - 1] > last:
                x += abs(vec[n - 1] - last)
            elif last < 0 and vec[n - 1] > 0:
                x += abs(vec[n - 1])
            elif last >= 0 and vec[n - 1] < 0:
                x += abs(vec[n - 1])
            elif last < 0 and vec[n - 1] < 0 and vec[n - 1] < last:
                x += abs(vec[n - 1] - last)
        
        return x