# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.validate(s, 0, {})

    def validate(self, s: str, opened: int, memo: dict[tuple[str, int], bool]) -> bool:
        for i, c in enumerate(s):
            if opened == 0 and c == ")":
                return False
            if c == "*":
                substring = s[i + 1 :]
                left_arg = (substring, opened + 1)
                left_valid = memo[left_arg] if left_arg in memo else self.validate(*left_arg, memo)
                memo[left_arg] = left_valid
                if left_valid:
                    return True
                if opened > 0:
                    right_arg = (substring, opened - 1)
                    right_valid = memo[right_arg] if right_arg in memo else self.validate(*right_arg, memo)
                    memo[right_arg] = right_valid
                    if right_valid:
                        return True
            else:
                if c == "(":
                    opened += 1
                else:
                    opened -= 1

        return opened == 0
