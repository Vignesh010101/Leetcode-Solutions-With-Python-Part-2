class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        loss = []
        win = []
        for t in transactions:
            if t[0]-t[1] > 0:
                loss.append(t)
            else:
                win.append(t)
        loss = sorted(loss, key=lambda x: x[1])
        win = sorted(win, key=lambda x: x[0], reverse=True)
        loss += win
        s = 0
        m = 0
        for l in loss:
            s += l[0]
            if s > m:
                m = s
            s -= l[1]
        return m