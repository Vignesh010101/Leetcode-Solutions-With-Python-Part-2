class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ll = len(changed)
        if ll % 2 != 0: return []
        result, hashmap = [], {}
        for n in changed: hashmap[n] = 1 + hashmap.get(n, 0)
        for num in sorted(hashmap.keys()):
            if hashmap[num] > 0:
                if num == 0:
                    if hashmap[num] % 2 != 0: return []
                    result += [0] * (hashmap[num] // 2)
                    hashmap[num] = 0
                elif hashmap.get(num * 2, False):
                    if hashmap[num] > hashmap[num*2]: return []
                    count = hashmap[num]
                    hashmap[num * 2] -= count
                    result += [num] * count 
        return result if len(result) == ll / 2 else []
