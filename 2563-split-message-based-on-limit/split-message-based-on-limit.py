import math


class Solution:
    def getNumberOfParts(self, message: str, limit: int) -> int:
        if limit < 6:
            return 0
        length = len(message)
        parts = math.ceil(length / (limit - 5))
        if 10 <= parts < 100:
            parts = math.ceil((length - 9) / (limit - 7)) if limit > 7 else 0
        if 100 <= parts < 1000:
            parts = math.ceil((length - 108) / (limit - 9)) if limit > 9 else 0
        if 1000 <= parts < 10000:
            parts = math.ceil((length - 1107) / (limit - 11)) if limit > 11 else 0
        if parts > 10000:
            parts = math.ceil((length + 118894) / limit)
            if parts > 10000:
                parts = 0
        return parts

    def splitMessage(self, message: str, limit: int) -> List[str]:
        res = []
        start, end = 0, 0
        parts = self.getNumberOfParts(message, limit)
        for i in range(parts):
            suffix = f"<{i+1}/{parts}>"
            end = start + limit - len(suffix)
            res.append(f"{message[start:end]}{suffix}")
            start = end
        return res