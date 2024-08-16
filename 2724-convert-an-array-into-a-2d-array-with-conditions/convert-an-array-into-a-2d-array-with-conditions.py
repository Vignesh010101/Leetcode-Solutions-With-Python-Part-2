class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while nums:
            cur = set()
            for i in range(len(nums)-1, -1, -1):
                if nums[i] not in cur:
                    cur.add(nums[i])
                    nums.pop(i)
            res.append(list(cur))
        return res