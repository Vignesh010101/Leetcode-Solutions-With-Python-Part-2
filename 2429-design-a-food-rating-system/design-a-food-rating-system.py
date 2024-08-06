TOMBSTONE = 'DELETED'

class CuisineRatings:
    def __init__(self):
        self.h = []
        self.d = {}
    
    def changeRating(self, food: str, newRating: int) -> None:
        if food in self.d:
            self.d[food][1] = TOMBSTONE
        pairlist = [-newRating, food]
        heappush(self.h, pairlist)
        self.d[food] = pairlist
    
    def highestRated(self) -> str:
        while self.h[0][1] == TOMBSTONE:
            heappop(self.h)
        return self.h[0][1]
        
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(CuisineRatings)
        self.cuisineMap = dict()
        for (food, cuisine, rating) in zip(foods, cuisines, ratings):
            self.cuisineMap[food] = cuisine
            self.cuisines[cuisine].changeRating(food, rating)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.cuisineMap[food]
        self.cuisines[cuisine].changeRating(food, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine].highestRated()

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)