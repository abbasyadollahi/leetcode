# https://leetcode.com/problems/basic-calculator/


class Solution:
    def calculate(self, s: str) -> int:
        self.i = 0
        self.s = s
        self.n = len(s)
        self.operations = {
            "-": lambda x, y: x - y,
            "+": lambda x, y: x + y,
        }

        return self.calculate_group()

    def calculate_group(self) -> int:
        group = 0
        op = "+"
        num_start = num_end = None
        while self.i < self.n:
            value = self.s[self.i]
            self.i += 1
            if value.isdigit():
                if num_start is None:
                    num_start = self.i - 1
                num_end = self.i
            elif value == "(":
                group = self.operations[op](group, self.calculate_group())
                op = "+"
            elif value == ")":
                if num_start is None:
                    return group
                else:
                    return self.operations[op](group, int(self.s[num_start:num_end]))
            elif value in self.operations:
                if num_start is not None:
                    group = self.operations[op](group, int(self.s[num_start:num_end]))
                    op = "+"
                    num_start = num_end = None

                if op == value:
                    op = "+"
                else:
                    op = "-"

        if num_start is not None:
            group = self.operations[op](group, int(self.s[num_start:num_end]))

        return group
