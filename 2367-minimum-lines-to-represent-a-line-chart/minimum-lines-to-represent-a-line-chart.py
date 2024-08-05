import math
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices = sorted(stockPrices, key=lambda xy: xy[0])

        num_lines = 0
        curr_line = None
        for i in range(1, len(stockPrices)):
            x1, y1 = stockPrices[i]
            if curr_line is None:
                x0, y0 = stockPrices[i-1]
                dx = x1 - x0
                dy = y1 - y0

                curr_line = (dx, dy, x0, y0)
                num_lines += 1
            else:
                dxl, dyl, xl, yl = curr_line
                dxl0 = x1 - xl
                dyl0 = y1 - yl
                if dxl0 * dyl != dyl0 * dxl:
                    x0, y0 = stockPrices[i-1]
                    dx = x1 - x0
                    dy = y1 - y0

                    curr_line = (dx, dy, x0, y0)
                    num_lines += 1

        return num_lines