# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate('(', n - 1, 1)

    def generate(self, parentheses: str, n: int, opened: int) -> List[str]:
        new = []
        if n:
            new.extend(self.generate(parentheses + '(', n - 1, opened + 1))
        elif opened:
            new.extend(self.generate(parentheses + ')', n, opened - 1))
        else:
            new.append(parentheses)

        if n and opened:
            new.extend(self.generate(parentheses + ')', n, opened - 1))
        return new
