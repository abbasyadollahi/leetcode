# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        priorities = dict(zip(order, range(len(order))))
        return words == sorted(words, key=lambda word: list(map(priorities.get, word)))
