class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:

        items.sort(reverse = True)
        sm, seenCats, dups = 0, set(), deque()

        for headPrf, headCat in items[:k]:
            
            sm+= headPrf

            if headCat in seenCats: dups.append(headPrf)
            else: seenCats.add(headCat)

        numCats = len(seenCats)    

        ans = sm = sm + numCats*numCats
        
        for tailPrf, tailCat in items[k:]:

            if not dups or tailCat in seenCats: continue
            numCats+= 1
            diff = tailPrf - dups.pop() + 2 * numCats - 1
                                       # a**2 - (a-1)**2 -  = 2*a - 1
            sm += diff  
            if diff > 0: ans = sm
            seenCats.add(tailCat)

        return ans