class Solution:
    def countPairs(self, nums: List[int]) -> int:

        def flip_ch(i: int, j: int)-> None:

            if num[i] == num[j]: return
            num[i], num[j] = num[j], num[i]

            s = ''.join(num)

            if  next[s] < idx + 1:
                next[s] = idx + 1
                frst[s] += 1

            return


        frst, next, res = defaultdict(int), defaultdict(int), 0

        mx = int(log10(max(nums)))+1
        nums = list(map(lambda x: (str(x).rjust(mx, '0')), nums))

        for idx, num in enumerate(nums):

            res+= frst[num]
            frst[num]+= 1
            next[num] = idx + 1
            num = list(num)

            for c1, c2 in combinations(range(mx), 2):
                
                flip_ch(c1, c2)

                for c3, c4 in combinations(range(c1, mx), 2):

                    flip_ch(c3, c4)
                    num[c3], num[c4] = num[c4], num[c3]

                num[c1], num[c2] = num[c2], num[c1]
        
        return res   