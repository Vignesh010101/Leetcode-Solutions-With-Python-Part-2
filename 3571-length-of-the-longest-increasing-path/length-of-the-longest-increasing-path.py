class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:

        less = lambda z: z[0] < max_x and z[1] < max_y
        grtr = lambda z: z[0] > max_x and z[1] > max_y
        ordr = lambda z: (z[0], -z[1])

        def lis(arr):

            res = []
            for _,y in arr:

                if not res or y > res[-1]: res.append(y)
                else: res[bisect_left(res, y)] = y
            
            return len(res)
        

        max_x, max_y = coordinates[k]

        left = lis(sorted(filter(less, coordinates),key = ordr))
        rght = lis(sorted(filter(grtr, coordinates),key = ordr))

        return left + 1 + rght