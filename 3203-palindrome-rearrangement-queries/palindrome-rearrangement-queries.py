class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        m = n // 2
        # split in 2 and reverse second
        s1, s2 = s[:m], s[m:][::-1]
        
        arr = []
        for i in range(m):
            if s1[i] != s2[i]:
                arr.append(i)
        
        # store prefix char count before pos 'i'. 
        count1 = [[0]*26]
        count2 = [[0]*26]
        orda = ord('a')
        for i in range(m):
            count1.append(count1[-1][::])
            count2.append(count2[-1][::])
            pos1 = ord(s1[i]) - orda
            pos2 = ord(s2[i]) - orda
            count1[-1][pos1] += 1
            count2[-1][pos2] += 1
        
        # no differences. Return True
        if not arr:
            return [True]*len(queries)
        
        # checks that chars in range [a..b] are same in both s1 & s2
        def checkChars(a, b):
            for i in range(26):
                if count1[b+1][i]-count1[a][i] != count2[b+1][i]-count2[a][i]:
                    return False
            return True

        def checkIntersectChars(a,b,c,d):
            c1, c2 = count1, count2
            # change order [a..b] to start first
            if c < a:
                a, b, c, d = c, d, a, b
                c1, c2 = c2, c1
            # [a..b] covers everything
            if b >= d:
                return checkChars(a,b)
            # [c..d] covers everything
            if c <= a:
                return checkChars(c,d)
            
            # checking chars in full range
            if not checkChars(min(a,c), max(b,d)):
                return False
            
            # checking each separate range to see that it has enough chars.
            # s1[a..b] should have enough chars to build s2[a..(c-1)]
            # same on the opposite side. s2[c..d] should have enough chars to build s1[(b+1)..d]
            # chars in the intersecting area are covered by above check.
            for i in range(26):
                if c1[b+1][i]-c1[a][i] < c2[c][i]-c2[a][i]:
                    return False
                if c2[d+1][i]-c2[c][i] < c1[d+1][i]-c1[b+1][i]:
                    return False
            return True
                

        # check that ranges [a..b] and [c..d] include all chars that are different in s1 & s2
        def checkCover(a,b,c,d):
            if c < a:
                a, b, c, d = c, d, a, b
            # range intersection. we can join the ranges.
            if c <= b:
                # check edges
                if min(a, c) > arr[0] or max(b, d) < arr[-1]:
                    return False
                else:
                    return True
                
            # check edges
            if a > arr[0] or d < arr[-1]:
                return False
            # check between ranges
            pos = bisect.bisect_right(arr,b)
            if pos < len(arr) and arr[pos] < c:
                return False
            return True
                
        res = []
        for i, [a,b,c,d] in enumerate(queries):
            # reverting order. if it's last 2 chars [n-2, n-1] it becomes first 2 in reverse [0,1]
            c, d = n-d-1, n-c-1, 
            
            if not checkCover(a,b,c,d):
                res.append(False)
                continue

            # no intersection between ranges
            if b < c or d < a:
                res.append(checkChars(a,b) and checkChars(c,d))
                continue
            
            # intersection
            res.append(checkIntersectChars(a,b,c,d))

        return res