# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        groupings = {}
        for word in words:
            anagram = ''.join(sorted(word))
            groupings[anagram] = groupings.get(anagram, []) + [word]

        return list(groupings.values())

sol = Solution()
print(sol.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print([['bat'], ['nat','tan'], ['ate','eat','tea']])
