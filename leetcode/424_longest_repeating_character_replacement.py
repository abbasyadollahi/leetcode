# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        longest = 0
        length = len(s)

        while l < length and r < length:
            l_next = None
            l_letter = s[l]
            replacements = k
            while replacements >= 0 and r < length:
                if s[r] != l_letter:
                    replacements -= 1
                    l_next = l_next or r
                r += 1
            if replacements > 0:
                r += min(l, replacements)
            elif replacements < 0:
                r -= 1
            longest = max(longest, r - l)
            l = r = l_next or r

        return longest

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = Counter()
        max_count = 0

        for r, c in enumerate(s):
            count[c] += 1

            replacements = 1 + r - l - count.most_common(1)[0][1]
            if replacements > k:
                count[s[l]] -= 1
                l += 1

            max_count = max(max_count, 1 + r - l)

        return max_count
