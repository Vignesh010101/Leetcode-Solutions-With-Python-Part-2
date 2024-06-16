class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(k) -> bool:
            # take the FIRST k elements from removable
            removable_set = set(removable[:k])
            count = 0
            for i in range(len(s)):
                if i in removable_set:
                    continue
                if s[i] == p[count]:
                    count += 1
                    if count == len(p):
                        return True
            return False
        # binary search for k
        res = 0
        left, right = 1, len(removable)
        while left <= right:
            mid = (left + right)//2
            if is_subsequence(mid):
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1
        return res