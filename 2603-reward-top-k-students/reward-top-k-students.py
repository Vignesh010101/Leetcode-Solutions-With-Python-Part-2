import heapq

class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        top_scorers = [(-float('inf'), -float('inf'))] * k  # Min Heap
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        for report_string, sid in zip(report, student_id):
            score = 0
            report_words = report_string.split()
            for word in report_words:
                if word in positive_feedback:
                    score += 3
                if word in negative_feedback:
                    score -= 1
            heapq.heappushpop(top_scorers, (score, -sid))

        ans = []
        for _ in range(k):
            _, sid = heapq.heappop(top_scorers)
            ans.append(-sid)

        return ans[::-1]  # Return reversed `ans` i.e. non-decreasing