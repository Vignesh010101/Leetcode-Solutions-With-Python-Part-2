class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        a = deque([])
        j = 0
        for i in range(len(pushed)):
            a.appendleft(pushed[i])
            while(a and a[0] == popped[j]):
                a.popleft()
                j+=1
        return not a