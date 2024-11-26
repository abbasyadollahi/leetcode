# https://leetcode.com/problems/alien-dictionary/

from collections import defaultdict


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        pre = defaultdict(set)
        suc = defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break

        chars = set("".join(words))
        charToProcess = chars - set(pre)
        order = ""
        while charToProcess:
            ch = charToProcess.pop()
            order += ch
            for b in suc[ch]:
                pre[b].discard(ch)
                if not pre[b]:
                    charToProcess.add(b)
        return order * (set(order) == chars)


sol = Solution()
print(sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
