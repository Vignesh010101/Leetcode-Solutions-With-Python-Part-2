class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        result = [0 for _ in range(len(A))]
        count = 0
        for i in range(len(A)):
            if A[i] == B[i]:
                count += 1
            if A[i] in set_b and B[i] in set_a:
                count += 2
            elif A[i] in set_b and B[i] not in set_a:
                count += 1
                set_a.add(A[i])
                set_b.add(B[i])
            elif A[i] not in set_b and B[i] in set_a:
                count += 1
                set_a.add(A[i])
                set_b.add(B[i])
            set_a.add(A[i])
            set_b.add(B[i])
            result[i] = count
        return result
        