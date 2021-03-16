# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
    def longestSubstringKChar(self, s: str, k: int) -> int:
        if not s or not k:
            return 0

        count = 0
        max_count = 0
        chars = []
        substring = ''

        for c in s:
            if c not in chars:
                chars.append(c)
                if len(chars) <= k:
                    substring += c
                    count += 1
                else:
                    chars.pop(0)
                    substring = self.stripOneUniqueChar(substring, k) + c
                    max_count = max(count, max_count)
                    count = len(substring)
            else:
                substring += c
                count += 1

        return max(count, max_count)

    def stripOneUniqueChar(self, substring: str, k: int) -> str:
        k -= 1
        chars = set()
        stripped = ''
        i = len(substring) - 1

        while i >= 0 and (len(chars) < k or substring[i] in chars):
            stripped += substring[i]
            chars.add(substring[i])
            i -= 1

        return stripped[::-1]

sol = Solution()
print(sol.longestSubstringKChar('eceba', 0))
print(sol.longestSubstringKChar('eceba', 2))
print(sol.longestSubstringKChar('aabbccccc', 2))
print(sol.longestSubstringKChar('abcadcacacaca', 1))
print(sol.longestSubstringKChar('aaqsskaksadkbsaddb', 3))
print(sol.longestSubstringKChar('aaqsskaksadkbsaddb', 4))
