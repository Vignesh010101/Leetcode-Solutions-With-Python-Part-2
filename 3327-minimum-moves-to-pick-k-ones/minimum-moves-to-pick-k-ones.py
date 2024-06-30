class Solution:
    def minimumMoves(self, nums: List[int], k: int, max_changes: int) -> int:
        s = "".join(map(str, nums))
        if "111" in s:
            max_cons = 3
        elif "11" in s:
            max_cons = 2
        elif "1" in s:
            max_cons = 1
        else:
            max_cons = 0

        if max_cons > k:
            max_cons = k
        if max_changes >= k - max_cons:
            return (k - max_cons) * 2 + max(0, max_cons - 1)
        
        res = max_changes * 2
        k -= max_changes
        idxes = [i for i in range(len(nums)) if nums[i]]
        pmid = k // 2
        left = 0
        cdiff = mdiff = sum(abs(i - idxes[pmid]) for i in idxes[:k])
        for right in range(k, len(idxes)):
            cdiff -= idxes[pmid] - idxes[left]
            left += 1
            cdiff += idxes[right] - idxes[pmid + 1]
            move_d = idxes[pmid + 1] - idxes[pmid]
            cdiff += ((pmid + 1 - left) - (right - 1 - pmid)) * move_d
            mdiff = min(mdiff, cdiff)
            pmid += 1
        res += mdiff
        return res