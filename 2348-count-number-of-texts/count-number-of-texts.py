class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        ans = 1
        modulo = 10 ** 9 + 7
        
        # Sequences of digits with 3 & 4 letters
        seqs = {3: [], 4: []}
        
        # DP for basic cases
        dp = {
            3: [1, 2, 4],  # Keys with 3 letters (2, 3, 4, 5, 6, 8)
            4: [1, 2, 4, 8]  # Keys with 4 letters (7, 9)
        }
        
        # Append and store sequences of 7 and 9 separately
        def appendSeq(key):
            seqs[4 if key in {'7', '9'} else 3].append(curSeq)

        # Iterate the pressed keys and store the length of each subsequence
        curSeq, curKey = 1, pressedKeys[0]
        for key in pressedKeys[1:]:
            if not curKey == key:
                appendSeq(curKey)
                curKey, curSeq = key, 0
            curSeq += 1
        appendSeq(curKey)
        
        for k in seqs.keys():
            # Update the DP with new sequences (only consider the maximum seqeunce length)
            if seqs[k]:
                for i in range(k, max(seqs[k])):
                    dp[k].append(sum(dp[k][(i - k):i]) % modulo)

            # Update the final result using DP & given modulo
            for seq in seqs[k]:
                ans *= dp[k][seq - 1]
                ans %= modulo

        return ans