class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        horizontalCut.sort(reverse = True)
        verticalCut.sort(reverse = True)

        h_i, v_i = 0, 0
        h_count, v_count = 1, 1 
        result = 0

        while h_i < m - 1 and v_i < n - 1:
            if horizontalCut[h_i] >= verticalCut[v_i]:
                result += horizontalCut[h_i] * v_count
                h_count += 1
                h_i += 1
            else:
                result += verticalCut[v_i] * h_count
                v_count += 1
                v_i += 1

        while h_i < m - 1:
            result += horizontalCut[h_i] * v_count
            h_count += 1
            h_i += 1

        while v_i < n - 1:
            result += verticalCut[v_i] * h_count
            v_count += 1
            v_i += 1

        return result