# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        substring = set()
        for c in s:
            if c in substring:
                max_length = max(max_length, len(substring))
                while c in substring:
                    substring.remove(s[l])
                    l += 1
            substring.add(c)

        return max(max_length, len(substring))
