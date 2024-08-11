class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        score.sort(key=lambda x: x[k], reverse=True)
        return score