class Solution:
    def minCharacters(self, a, b):
        ansa, ansb = [0]*26, [0]*26 

        for i in a:
            ansa[ord(i)-97] += 1 

        for i in b:
            ansb[ord(i)-97] += 1 

        da, db = sum(ansa), sum(ansb)
        res = da+db-max(ansa)-max(ansb)

        for i in range(25):
            da += ansb[i]-ansa[i]
            db += ansa[i]-ansb[i]
            res = min(res,da,db)

        return res 