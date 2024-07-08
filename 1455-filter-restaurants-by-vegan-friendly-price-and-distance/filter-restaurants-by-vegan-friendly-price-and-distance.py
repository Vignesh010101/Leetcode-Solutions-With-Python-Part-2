class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        rating=[]
        res=[]
        for restro in restaurants:
            if (restro[3]<=maxPrice) and (restro[4]<=maxDistance):
                if (veganFriendly):
                    if restro[2]==1:
                        rating.append([restro[1],restro[0]])
                else:
                    rating.append([restro[1],restro[0]])
        rating.sort()
        for i in rating:
            res.append(i[1])
        res.reverse()
        return res
        