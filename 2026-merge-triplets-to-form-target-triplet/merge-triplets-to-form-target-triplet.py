class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_vals = [0, 0, 0]

        for t in triplets:
            if all(t[i] <= target[i] for i in range(len(target))):
                for i in range(len(target)):
                    if t[i] == target[i]:
                        max_vals[i] = t[i]
            
            if max_vals == target:
                break
        
        return max_vals == target