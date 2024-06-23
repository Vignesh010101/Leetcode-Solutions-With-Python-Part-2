from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        tree = SortedList(nums[2:2+dist])
        ans = cost = nums[0] + nums[1] + sum(tree.islice(0, k-2))
        n = len(nums)
        for i in range(2,n - (k-2)):
            cost = cost - nums[i-1] + nums[i]
            p = tree.bisect_right(nums[i]) - 1
            tree.pop(p)
            if i + dist < n and k - 2 >= dist:
                cost = cost - nums[i] + nums[i+dist]
            else:
                if p < k - 2:
                    cost = cost - nums[i] + tree[k-2-1]
                if i + dist < n:
                    if nums[i+dist] < tree[k-2-1]:
                        cost = cost - tree[k-2-1] + nums[i+dist]
            if i + dist < n:
                tree.add(nums[i+dist]) 
            ans = min(ans, cost)    
        return ans