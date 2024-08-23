class Solution:
    def minimumOperations(self, num: str) -> int:
        res = math.inf
        pairs = {'0':['0','5'], '5':['2', '7']}
        jj = -1
        ii = -1
        for i in range(len(num)-1,-1,-1):
            if num[i] in pairs.keys():
                ii = num[i]
                for j in range(i-1,-1,-1):
                    if num[j] in pairs[num[i]]: 
                        res = min(res, len(num)-j-2)
                        jj = num[j]

        
        if jj == -1:
            if ii == '0':
                res = min(res, len(num)-1) 
            if ii == -1 or ii == '5':
                res = min(res, len(num))
    
            
            
        return res