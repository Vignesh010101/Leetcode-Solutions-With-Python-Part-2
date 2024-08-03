class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic = {}
        #construct a dictionary of dificulty occurence
        for item in tasks:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        
        count = 0
        for idx, val in dic.items():
            # return if value is 1
            if val == 1:
                return -1
            
            # calculate round
            if val%3 == 0:
                count += val//3
            else:
                count += (val // 3) + 1
        
        return count