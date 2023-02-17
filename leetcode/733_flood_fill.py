# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.fill(image, sr, sc, image[sr][sc], color)
        return image

    def fill(self, image: list[list[int]], r: int, c: int, original: int, color: int) -> None:
        if r not in range(0, len(image)):
            return
        if c not in range(0, len(image[0])):
            return
        if image[r][c] != original:
            return
        if image[r][c] == color:
            return

        image[r][c] = color
        self.fill(image, r - 1, c, original, color)
        self.fill(image, r + 1, c, original, color)
        self.fill(image, r, c - 1, original, color)
        self.fill(image, r, c + 1, original, color)
