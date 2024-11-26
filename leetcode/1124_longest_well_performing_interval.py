# https://leetcode.com/problems/longest-well-performing-interval/


class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        score = 0
        scores = []
        indexes = {}

        for index, hour in enumerate(hours):
            score += (-1) ** (hour <= 8)
            scores.append(score)
            indexes[score] = indexes.get(score, index)

        return max(index if score > 0 else index - indexes.get(score - 1, index) for index, score in enumerate(scores))
