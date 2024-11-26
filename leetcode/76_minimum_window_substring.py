# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = deque()
        count = Counter()
        count.subtract(Counter(t))

        l = 0
        substring = ""
        length = float("inf")

        for r, c in enumerate(s):
            if c not in count:
                continue

            count[c] += 1
            seen.append((r, c))

            if c == seen[0][1]:
                while count[c] > 0:
                    count[c] -= 1
                    seen.popleft()
                    l, c = seen[0]

            if length > (r - l) and len(-count) == 0:
                l = seen[0][0]
                substring = s[l : r + 1]
                length = len(substring)

        return substring
