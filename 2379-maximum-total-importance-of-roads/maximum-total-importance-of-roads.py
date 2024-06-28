class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr=[0]*n
        for v,y in roads:
            arr[v]+=1
            arr[y]+=1
        arr.sort()
        summ=0
        for i in range(len(arr)):
            summ+=arr[i]*(i+1)

        return summ