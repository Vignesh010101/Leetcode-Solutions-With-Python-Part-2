class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        max_score = nums.count(1)
        current_score = max_score
        max_score_indices = [0]
        for index, num in enumerate(nums):
            if num == 0:
                current_score += 1
            else:
                current_score -= 1
            if current_score > max_score:
                max_score = current_score
                max_score_indices = [index + 1]
            elif current_score == max_score:
                max_score_indices.append(index + 1)
        return max_score_indices