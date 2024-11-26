# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:
    def __init__(self) -> None:
        self.size = 0
        self.index_to_numbers = {}
        self.numbers_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.numbers_to_index:
            return False
        else:
            self.size += 1
            self.numbers_to_index[val] = self.size
            self.index_to_numbers[self.size] = val
            return True

    def remove(self, val: int) -> bool:
        if val not in self.numbers_to_index:
            return False
        elif val == self.index_to_numbers[self.size]:
            self.index_to_numbers.pop(self.size)
            self.numbers_to_index.pop(val)
            self.size -= 1
            return True
        else:
            top_value = self.index_to_numbers.pop(self.size)
            self.numbers_to_index.pop(top_value)
            self.size -= 1

            index = self.numbers_to_index.pop(val)
            self.index_to_numbers.pop(index)

            self.numbers_to_index[top_value] = index
            self.index_to_numbers[index] = top_value
            return True

    def getRandom(self) -> int:
        index = random.randint(1, self.size)
        return self.index_to_numbers[index]
