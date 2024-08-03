class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        l = len(tiles)
        cover = 0
        j = 0
        ans = 0
        tiles.sort()
        for i in range(l):
            l_start, r_start = tiles[i]
            len_start = r_start - l_start + 1
            if len_start >= carpetLen:
                return carpetLen           
            while j < l and tiles[j][1] - l_start + 1 <= carpetLen:
                cover += tiles[j][1] - tiles[j][0] + 1
                j += 1
            if j == l:
                return max(ans, cover)
            else:
                ans = max(ans, cover+max(carpetLen+l_start-tiles[j][0],0))
            cover -= len_start
        return ans