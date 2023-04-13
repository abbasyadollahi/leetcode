# https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.location = 0

    def visit(self, url: str) -> None:
        self.location += 1
        self.history[self.location:] = [url]

    def back(self, steps: int) -> str:
        self.location = max(self.location - steps, 0)
        return self.history[self.location]

    def forward(self, steps: int) -> str:
        self.location = min(self.location + steps, len(self.history) - 1)
        return self.history[self.location]
