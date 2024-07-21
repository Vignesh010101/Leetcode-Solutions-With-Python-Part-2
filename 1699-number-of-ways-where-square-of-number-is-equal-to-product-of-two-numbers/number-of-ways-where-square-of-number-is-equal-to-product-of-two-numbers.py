class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        vs1 = list(c1.keys())
        vs2 = list(c2.keys())
        vs1.sort()
        vs2.sort()

        def count(left, lvals, right, rvals):
            ans = 0

            for vi, fi in left.items():
                for vj in rvals:
                    if vj >= vi: break
                    if vi**2 % vj == 0:
                        fj = right[vj]
                        fk = right.get(vi**2//vj, 0)
                        ans += fi*fj*fk
                
                if vj == vi:
                    fj = right[vj]
                    ans += fi*(fj*(fj-1))//2

            return ans

        return count(c1, vs1, c2, vs2) + count(c2, vs2, c1, vs1)