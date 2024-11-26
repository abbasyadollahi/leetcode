# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        groupings = {}
        for word in words:
            anagram = "".join(sorted(word))
            groupings[anagram] = groupings.get(anagram, []) + [word]

        return list(groupings.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
