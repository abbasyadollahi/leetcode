# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        opening = list('[{(')
        closing = list(']})')
        for bracket in s:
            if bracket in opening:
                brackets.append(bracket)
            elif not brackets or opening.index(brackets.pop()) != closing.index(bracket):
                return False
        return not brackets

    def isValid(self, s: str) -> bool:
        opened = []
        brackets = dict(zip('[{(', ']})'))
        for bracket in s:
            if bracket in brackets:
                opened.append(bracket)
            elif not opened or brackets[opened.pop()] != bracket:
                return False
        return not opened
