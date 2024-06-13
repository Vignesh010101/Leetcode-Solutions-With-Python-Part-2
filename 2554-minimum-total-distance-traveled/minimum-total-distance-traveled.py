from scipy import optimize
import numpy

class Solution:
    def minimumTotalDistance(self, rs: List[int], fs: List[List[int]]) -> int:
        costs = []
        for i, k in fs:
            c = [abs(j-i) for j in rs]
            for _ in range(k):
                costs.append(c)
        costs = numpy.array(costs)
        return costs[optimize.linear_sum_assignment(costs)].sum() 
        