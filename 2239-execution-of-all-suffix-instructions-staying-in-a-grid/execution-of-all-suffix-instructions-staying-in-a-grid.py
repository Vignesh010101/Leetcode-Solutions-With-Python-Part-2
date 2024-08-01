class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        k = 0
        ans = []
        for k in range(m):
            st = s[k:m]
            count = 0
            i, j = startPos
            for char in st:
                if char == "R":
                    if j + 1 < n:
                        count += 1
                        j += 1
                    else:
                        break

                elif char == "D":
                    if i + 1 < n:
                        count += 1
                        i += 1
                    else:
                        break

                elif char == "L":
                    if j - 1 >= 0:
                        j -= 1
                        count += 1
                    else:
                        break

                elif char == "U":
                    if i - 1 >= 0:
                        i -= 1
                        count += 1
                    else:
                        break

            ans.append(count)

        return ans