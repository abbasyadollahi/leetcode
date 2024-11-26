# https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = sum(map(str.isupper, word))
        return (count in [0, len(word)]) or (count == 1 and word[0].isupper())
