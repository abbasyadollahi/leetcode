# https://leetcode.com/problems/word-break/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        matches = [True] + [False] * n
        wordDict = set(wordDict)

        for i, c in enumerate(s, 1):
            matches[i] = any(matches[j] and s[j:i] in wordDict for j in range(i))

        return matches[n]
