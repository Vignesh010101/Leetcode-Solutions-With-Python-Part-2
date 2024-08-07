class Solution:
    from collections import defaultdict
    def getFolderNames(self, names: List[str]) -> List[str]:
        used, hashmap = set(), defaultdict(int)
        result = []
        for name in names:
            k = hashmap[name]
            current = name
            while current in used:
                k += 1
                current = '%s(%d)' % (name, k)  # alternative to current = name+'('+str(k)+')'
            hashmap[name] = k
            result.append(current)
            used.add(current)
        return result