class Log:
    def __init__(self, log):
        self.log = log

    def __eq__(self, other):
        return self.log == other.log

    def __lt__(self, other):
        id1, *rest1 = self.log.split(" ")
        id2, *rest2 = other.log.split(" ")
        if rest1 == rest2:
            return id1 < id2
        else:
            return " ".join(rest1) < " ".join(rest2)

    def __gt__(self, other):
        id1, *rest1 = self.log.split(" ")
        id2, *rest2 = other.log.split(" ")
        if rest1 == rest2:
            return id1 > id2
        else:
            return " ".join(rest1) > " ".join(rest2)

    def __repr__(self):
        return self.log


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digit_logs, letter_logs = [], []
        for log in logs:
            identifier, first, *rest = log.split(" ")
            if first.isdigit():
                digit_logs.append(log)
            else:
                log = Log(log)
                bisect.insort(letter_logs, log)
        
        return [l.log for l in letter_logs] + digit_logs
            