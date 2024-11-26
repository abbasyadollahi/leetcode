# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return self.generate("(", n - 1, 1)

    def generate(self, parentheses: str, n: int, opened: int) -> list[str]:
        new = []
        if n:
            new.extend(self.generate(parentheses + "(", n - 1, opened + 1))
        elif opened:
            new.extend(self.generate(parentheses + ")", n, opened - 1))
        else:
            new.append(parentheses)

        if n and opened:
            new.extend(self.generate(parentheses + ")", n, opened - 1))
        return new
