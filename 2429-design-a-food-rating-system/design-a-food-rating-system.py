class FoodRatings:
    def __init__(
        self, foods: List[str], cuisines: List[str], ratings: List[int]
    ):
        self.ratings = {}
        self.food_to_cuisine = {}
        self.ratings_heaps = {}
        for i in range(len(foods)):
            if cuisines[i] not in self.ratings:
                self.ratings[cuisines[i]] = {}
            self.ratings[cuisines[i]][foods[i]] = ratings[i]
            self.food_to_cuisine[foods[i]] = cuisines[i]
            if cuisines[i] not in self.ratings_heaps:
                self.ratings_heaps[cuisines[i]] = []
            heapq.heappush(self.ratings_heaps[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[self.food_to_cuisine[food]][food] = newRating
        heapq.heappush(self.ratings_heaps[self.food_to_cuisine[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        rating, food = self.ratings_heaps[cuisine][0]
        while rating != -self.ratings[cuisine][food] and len(self.ratings_heaps[cuisine]) > 0:
            rating, food = heapq.heappop(self.ratings_heaps[cuisine])

        heapq.heappush(self.ratings_heaps[cuisine], (rating, food))

        return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)