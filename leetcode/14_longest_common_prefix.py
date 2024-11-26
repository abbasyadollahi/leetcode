# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        i = 0
        prefix = ""
        min_length = min(map(len, strs))

        while i < min_length:
            char = strs[0][i]
            for word in strs:
                if word[i] != char:
                    return prefix
            i += 1
            prefix += char

        return prefix
