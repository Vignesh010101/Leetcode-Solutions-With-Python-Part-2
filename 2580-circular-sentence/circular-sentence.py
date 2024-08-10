class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        last = words[len(words) - 1]
        if len(words) == 1 and words[0][0] == last[len(last) - 1]:
            return True
        else:
            for i in range(0, len(words) - 1):
                if words[i][len(words[i]) - 1] != words[i + 1][0]:
                    return False

            if words[0][0] == last[len(last) - 1]:
                return True