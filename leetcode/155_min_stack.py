# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack = [(float('inf'), float('inf'))]

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStack:
    def __init__(self):
        self.val_stack = [float('inf')]
        self.min_stack = [float('inf')]

    def push(self, val: int) -> None:
        self.val_stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.val_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
