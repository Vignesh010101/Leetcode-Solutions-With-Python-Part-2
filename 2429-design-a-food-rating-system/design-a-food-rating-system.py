from collections import defaultdict
import heapq

class Food():
    def __init__(self, food, rating):
        self.food = food
        self.rating = rating

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.food < other.food
        return self.rating > other.rating

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_lookup = defaultdict()
        self.food_rating = defaultdict()
        self.cuisine_lookup = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_lookup[food] = cuisine
            self.food_rating[food] = rating
            heapq.heappush(self.cuisine_lookup[cuisine], Food(food, rating))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        cuisine = self.food_lookup[food]
        heapq.heappush(self.cuisine_lookup[cuisine], Food(food, newRating))        

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_lookup[cuisine][0]
        while self.food_rating[highest_rated.food] != highest_rated.rating:
            heapq.heappop(self.cuisine_lookup[cuisine])
            highest_rated = self.cuisine_lookup[cuisine][0]
        return highest_rated.food
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)