# https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(set)
        for person, trusted in trust:
            trusts[person].add(trusted)

        judges = set(range(1, n + 1)) - trusts.keys()

        if len(judges) != 1:
            return -1

        judge = judges.pop()
        if all(judge in trusted for trusted in trusts.values()):
            return judge
        else:
            return -1

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = dict.fromkeys(range(1, n + 1), 0)
        for person, trusted in trust:
            trust_count[person] -= 1
            trust_count[trusted] += 1

        for person, count in trust_count.items():
            if count == n - 1:
                return person
        return -1
