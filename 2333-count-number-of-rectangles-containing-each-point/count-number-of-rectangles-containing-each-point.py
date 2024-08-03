from sortedcontainers import SortedList
from typing import List, Dict

class Solution:

    def binary_search(self, arr: SortedList, x: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (high + low) // 2

            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid

        return max(high, low)
    
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        y_to_xs: Dict[int, SortedList] = {}
        
        # Organize rectangles by their y-coordinates
        for x, y in rectangles:
            if y not in y_to_xs:
                y_to_xs[y] = SortedList()
            y_to_xs[y].add(x)
        
        result = []
        
        # Count the rectangles for each point
        for px, py in points:
            count = 0
            
            for y in range(py, 101):
                if y in y_to_xs:
                    xs = y_to_xs[y]
                    
                    if px <= xs[-1]:  # Only consider if px can be within bounds of xs
                        count += len(xs) - self.binary_search(xs, px)
            
            result.append(count)
        
        return result