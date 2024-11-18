class Solution:

    def equalizeQueue(self, n, k, multiplier):

            queue = [0] * len(n)
            prevPower = None
            
            for index, (logVal, num, originalIndex) in enumerate(n):
                currentPower = int(logVal)
            
                if multiplier ** (currentPower + 1) <= num:
                    #save ourselves from 2.0 (or 1.999999) rounding down to 1.0 accidentally because of floating point precision

                    currentPower += 1
                if index == 0:
                    prevPower = currentPower
                elif prevPower != currentPower:
                    #bring everything before us to this logval
                    multiplyCount = (currentPower - prevPower)
            
                    if k >= multiplyCount * index:
                        k -= multiplyCount * index
                        queue[index - 1] = multiplyCount
            
                    elif k >= index:
                        multiplyCount = k // index
                        k -= multiplyCount * index
                        queue[index - 1] = multiplyCount
                    prevPower = currentPower
                    if k < index:
                        return queue
            
            if k >= len(n):
                multiplyCount = k // len(n)
                k -= multiplyCount * len(n)
                queue[len(n) - 1] = multiplyCount
            return queue

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        n = []
        for index, num in enumerate(nums):
            #calculate the powers using the log function
            n.append((math.log(num, multiplier), num, index))

        n.sort()
        queue = self.equalizeQueue(n, k, multiplier)
        
        #apply multiplications queue, save how many times we have to multiply every element:
        multiplyBy = 0
        for i in range(len(n) - 1, -1, -1):
            logVal, num, originalIndex = n[i]
            multiplyBy += queue[i]
            k -= multiplyBy
            n[i] = (logVal + multiplyBy, originalIndex, num, multiplyBy)
        

        n.sort()
        
        for i in range(k):
            logVal, originalIndex, num, multiplyBy = n[i]
            n[i] = (logVal + 1, originalIndex, num, multiplyBy + 1)
        for logVal, originalIndex, num, multiplyBy in n:
            nums[originalIndex] =( num * pow(multiplier, multiplyBy, (10 ** 9 + 7)) )% (10 ** 9 + 7)
        return nums