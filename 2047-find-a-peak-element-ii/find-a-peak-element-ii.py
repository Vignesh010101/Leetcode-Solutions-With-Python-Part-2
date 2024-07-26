class Solution:

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        L, H = 0, len(mat) - 1
        while L <= H:
            mid = (L + H) // 2
            mid_row = mat[mid]
            max_pos = None
            max_val = float(-inf)
            for j in range(len(mid_row)):
                if mid_row[j] > max_val:
                    max_val = mid_row[j]
                    max_pos = j
            top_val = -1 if mid - 1 < 0 else mat[mid-1][max_pos]
            bottom_val = -1 if mid + 1 >= len(mat) else mat[mid+1][max_pos]
            if top_val < max_val and bottom_val < max_val:
                return [mid, max_pos]
            if top_val >= max_val:
                H = mid - 1
            elif bottom_val >= max_val:
                L = mid + 1
