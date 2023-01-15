# https://leetcode.com/problems/naming-a-company/

from collections import defaultdict
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        initials = defaultdict(set)
        for idea in ideas:
            initials[idea[0]].add(idea[1:])

        total = 0
        initials_keys = iter(set(initials.keys()))
        while initials:
            initial_a = next(initials_keys)
            suffixes_a = initials.pop(initial_a)
            for initial_b, suffixes_b in initials.items():
                if initial_a == initial_b:
                    continue

                matches = len(suffixes_a & suffixes_b)
                total += (len(suffixes_a) - matches) * (len(suffixes_b) - matches)

        return total * 2
