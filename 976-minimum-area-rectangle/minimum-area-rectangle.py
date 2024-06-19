class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        horizontal_lines = {}

        vertical_lines = {}

        min_area = float('inf')


        for x, y in points:

            if y not in horizontal_lines:

                horizontal_lines[y] = []

            horizontal_lines[y].append(x)

            if x not in vertical_lines:

                vertical_lines[x] = []
                
            vertical_lines[x].append(y)


        for line in horizontal_lines.values():

            line.sort()

        for line in vertical_lines.values():

            line.sort()


        for x, y in points:

            for prev_x in horizontal_lines[y]:

                if prev_x >= x:

                    continue

                for prev_y in vertical_lines[x]:

                    if prev_y >= y:

                        continue

                    if prev_y in vertical_lines[prev_x]:

                        min_area = min(min_area, abs(x - prev_x) * abs(y - prev_y))

        return 0 if min_area == float('inf') else min_area

        