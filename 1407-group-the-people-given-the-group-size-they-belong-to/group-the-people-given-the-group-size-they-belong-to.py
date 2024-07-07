class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic,res = {},[]
        for person, groupsize in enumerate(groupSizes):
            dic[groupsize] = dic.get(groupsize, []) + [person]      
        for key, lst in dic.items():
            groups = [lst[i:i+key] for i in range(0,len(lst),key)]
            res.extend(groups)
        return res

