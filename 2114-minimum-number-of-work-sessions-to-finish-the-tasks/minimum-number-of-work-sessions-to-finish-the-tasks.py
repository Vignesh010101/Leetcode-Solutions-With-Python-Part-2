class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        subsets = []
        self.ans = len(tasks)
        
        def func(idx):
            if len(subsets) >= self.ans:
                return
            
            if idx == len(tasks):
                self.ans = min(self.ans, len(subsets))
                return
            
            for i in range(len(subsets)):
                if subsets[i] + tasks[idx] <= sessionTime:
                    subsets[i] += tasks[idx]
                    func(idx + 1)
                    subsets[i] -= tasks[idx]
            
            subsets.append(tasks[idx])
            func(idx + 1)
            subsets.pop()
        
        func(0)
        return self.ans