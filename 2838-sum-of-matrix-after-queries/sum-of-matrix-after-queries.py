class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows, cols = [0] * (n + 1), [0] * (n + 1) 
        rows[-1], cols[-1] = n, n# last index stores length of hashset
        result = 0
        action_for_query = [(rows, cols), (cols, rows)]
        for query_type, index, value in reversed(queries):
            modified_axis, opposite_axis = action_for_query[query_type]
            if modified_axis[index] == 0:
                modified_axis[index] = 1 # 1 = used
                modified_axis[-1] -= 1 # decrease the count at the last index
                result += opposite_axis[-1] * value
        return result