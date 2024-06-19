class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L = 0
        max_fruit_count, fruit_count = 0, 0
        fruit_baskets = dict()

        for R in range(len(fruits)):
            fruit_baskets[fruits[R]] = fruit_baskets.get(fruits[R], 0) + 1
            fruit_count += 1

            while len(fruit_baskets) > 2:
                fruit_baskets[fruits[L]] -= 1
                fruit_count -= 1
                if fruit_baskets[fruits[L]] == 0:
                    fruit_baskets.pop(fruits[L])
                L += 1

            max_fruit_count = max(max_fruit_count, fruit_count)

        return max_fruit_count

    # O(n) time
    # O(1) space, at most two types of fruit baskets in HashMap