# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        substrings = {}
        for i, character in enumerate(s):
            substring = substrings.get(character, [i, i])
            substring[1] = i
            substrings[character] = substring

        return max(end - start for start, end in substrings.values()) - 1
