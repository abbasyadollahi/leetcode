# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tail = 0
        longest = 0
        seen = set()

        for char in s:
            if char in seen:
                longest = max(longest, len(seen))
                while s[tail] != char:
                    seen.remove(s[tail])
                    tail += 1
                tail += 1
            else:
                seen.add(char)
        return max(longest, len(seen))
