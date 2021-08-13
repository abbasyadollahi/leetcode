# https://leetcode.com/problems/reverse-words-in-a-string-ii/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split(' ')[::-1]) if s else ''


sol = Solution()
print(sol.reverseWords('the sky is blue'))
print(sol.reverseWords('I dropped my monster condom that I use for my magnum dong'))
print(sol.reverseWords(None))
