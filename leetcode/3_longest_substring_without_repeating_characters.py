# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        substring = set()
        for letter in s:
            while letter in substring:
                substring.remove(s[l])
                l += 1
            substring.add(letter)
            max_length = max(max_length, len(substring))

        return max_length
