class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, remain, current):
            if remain == 0:
                result.append(current[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remain:
                    break
                
                current.append(candidates[i])
                backtrack(i + 1, remain - candidates[i], current)
                current.pop()

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result