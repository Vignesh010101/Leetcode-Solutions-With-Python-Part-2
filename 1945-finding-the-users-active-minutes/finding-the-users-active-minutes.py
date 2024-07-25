class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        usersActiveMins = {}
        for log in logs:
            if log[0] in usersActiveMins:
                usersActiveMins[log[0]].add(log[1])
            else:
                usersActiveMins[log[0]] = {log[1]}
        
        answer = [0] * k

        for key in usersActiveMins:
            mins = len(usersActiveMins[key])
            if (mins):
                answer[mins-1] += 1
        
        return answer
        