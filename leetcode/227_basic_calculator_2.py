# https://leetcode.com/problems/basic-calculator-ii/


class Solution:
    def calculate(self, s: str) -> int:
        self.operations = {
            "-": lambda x: -x,
            "+": lambda x: x,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }

        return self.operate(self.parse(s.replace(" ", "")))

    def parse(self, s: str) -> list[str]:
        start = 0
        elements = []
        for i, c in enumerate(s):
            if c in self.operations:
                elements.append(s[start:i])
                elements.append(c)
                start = i + 1
        elements.append(s[start : i + 1])
        return elements

    def operate(self, elements: list[str]) -> int:
        nums = []
        operator = "+"
        for element in elements:
            if element.isdigit():
                if operator in ("+", "-"):
                    nums.append(self.operations[operator](int(element)))
                else:
                    nums.append(self.operations[operator](nums.pop(), int(element)))
            else:
                operator = element
        return sum(nums)
