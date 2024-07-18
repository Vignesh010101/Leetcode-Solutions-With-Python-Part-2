from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        @cache
        def check(n,target):
            nonlocal d
            if n == target:
                return True
            
            for e in d[n]:
                if check(e,target):
                    return True

            return False


        res = []
        d = defaultdict(list)
        for x,y in prerequisites:
            d[x].append(y)
        for x,y in queries:
            res.append(check(x,y))
       
        return res