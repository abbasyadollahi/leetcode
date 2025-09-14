# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        groups = {}
        for word in words:
            anagram = "".join(sorted(word))
            groups[anagram] = groups.get(anagram, []) + [word]

        return list(groups.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
