# https://leetcode.com/problems/fruit-into-baskets/

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruit_pairs = {}
        for first, second in zip(fruits, [*fruits, -1][1:]):
            if first != second and first not in fruit_pairs:
                fruit_pairs[first] = second

        left = 0
        right = 0
        current_fruits = 0
        max_fruits = 0
        fruit_count = defaultdict(int)
        while right < len(fruits):
            fruit_count[fruits[right]] += 1
            current_fruits += 1
            right += 1

            while len(fruit_count) > 2:
                if fruit_count[fruits[left]] == 1:
                    del fruit_count[fruits[left]]
                else:
                    fruit_count[fruits[left]] -= 1
                current_fruits -= 1
                left += 1

            max_fruits = max(max_fruits, current_fruits)

        return max_fruits
