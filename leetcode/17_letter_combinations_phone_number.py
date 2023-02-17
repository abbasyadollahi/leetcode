# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_letters = {
            '': list(),
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }
        if len(digits) in [0, 1]:
            return num_letters[digits]
        return [
            letter + combination
            for combination in self.letterCombinations(digits[1:])
            for letter in num_letters[digits[0]]
        ]
