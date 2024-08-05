class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_count = 0
        for i in range(len(arr)):
            if self.isDistinct(arr, i):
                distinct_count += 1
                if distinct_count == k:
                    return arr[i]
        return ""

    def isDistinct(self, arr: List[str], index: int) -> bool:
        return arr.count(arr[index]) == 1