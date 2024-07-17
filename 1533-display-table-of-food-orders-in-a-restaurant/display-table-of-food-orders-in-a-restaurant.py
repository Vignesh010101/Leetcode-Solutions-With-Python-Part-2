class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        a=set()
        b=set()
        for i in orders:
            a.add(i[2])
            b.add(i[1])
        a=list(a)
        b=list(b)
        a=sorted(a)
        b=sorted(b,key=lambda x:int(x))
        dic_a={}
        dic_b={}
        c=1
        for i in a :
            dic_a[i]=c
            c+=1
        c=1
        for i in b:
            dic_b[i]=c
            c+=1
        output=[]
        output.append(["Table"]+a)

        crx=["0" for i in range(len(a))]
        for i in b:
            output.append([i]+crx)
        
        for i in orders:
            output[dic_b[i[1]]][dic_a[i[2]]]=int(output[dic_b[i[1]]][dic_a[i[2]]])
            output[dic_b[i[1]]][dic_a[i[2]]]+=1
            output[dic_b[i[1]]][dic_a[i[2]]]=str(output[dic_b[i[1]]][dic_a[i[2]]])
        
        return output