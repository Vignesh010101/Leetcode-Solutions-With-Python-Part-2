class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        col={j[k]:i for i,j in enumerate(score)}
        x=sorted(col.items(),key=lambda col:col[0])
        a=[]
        while x:
            c=(score[x.pop()[1]])
            a.append(c)
        return a