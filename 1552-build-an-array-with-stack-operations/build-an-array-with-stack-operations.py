class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        vy=[]
        sc=[]
        for i in range(1,n+1):
            if i in target:
                sc.append(i)
                vy.append("Push")
                if sc==target:
                    return vy
                    break

            else:
                vy.append("Push")
                vy.append("Pop")

        return vy       