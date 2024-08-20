class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows, cols = set(i for i in range(n)), set(i for i in range(n))
        result = 0
        action_for_query = {0: (rows, cols), 1: (cols, rows)}
        for query_type, index, value in reversed(queries):
            modified_axis, opposite_axis = action_for_query[query_type]
            if index in modified_axis:
                modified_axis.remove(index)
                result += len(opposite_axis) * value
        return result