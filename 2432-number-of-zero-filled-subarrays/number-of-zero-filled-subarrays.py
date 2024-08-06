class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        aux = []
        resp = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                aux.append(nums[i])
            else:
                if len(aux) > 0:
                    n = len(aux)
                    resp += n*(n+1)/2
                    aux = []
        if len(aux) > 0:
            n = len(aux)
            resp += n*(n+1)/2
        return int(resp)