class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        return  (target>>maxDoubles)-1 + min(maxDoubles, target.bit_length()-1) + ((1<<maxDoubles)-1&target).bit_count()