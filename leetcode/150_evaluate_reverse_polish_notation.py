# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operations = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(x / y)
        }

        for token in tokens:
            if token in operations:
                numbers.append(operations[token](numbers.pop(), numbers.pop()))
            else:
                numbers.append(int(token))

        return numbers.pop()
