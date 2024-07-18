class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        list1=[x for x in range(1,n+1)]
        list2=[]
        list3=[]
        for i in range(len(list1)):
            list2.append("Push")
            list3.append(list1[i])
            if(list1[i] not in target):
                list2.append("Pop")
                list3.pop()
            elif(list3==target):
                break
        return list2

        