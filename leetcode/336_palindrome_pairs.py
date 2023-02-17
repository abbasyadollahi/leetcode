# https://leetcode.com/problems/palindrome-pairs/

class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        pairs = set()
        indexed = dict(zip(words, range(len(words))))

        for word, index in indexed.items():
            prefixes = [word[i:][::-1] for i in range(len(word) + 1) if is_palindrome(word[:i])]
            pairs.update((indexed[prefix], index) for prefix in prefixes if prefix in indexed and prefix != word)

            suffixes = [word[:i][::-1] for i in range(len(word) + 1) if is_palindrome(word[i:])]
            pairs.update((index, indexed[suffix]) for suffix in suffixes if suffix in indexed and suffix != word)

        return list(pairs)
