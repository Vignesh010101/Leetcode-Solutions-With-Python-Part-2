class Solution:
    def findScore(self, nums: List[int]) -> int:
        data = sorted(
            (elem, i)
            for i, elem in enumerate(nums)
        )

        score = 0
        marked = set()
        for elem, i in data:
            if i not in marked:
                marked.add(i - 1)
                marked.add(i + 1)
                score += elem
        return score