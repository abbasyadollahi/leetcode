# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winners = set()
        losers = defaultdict(int)

        for winner, loser in matches:
            winners.add(winner)
            losers[loser] += 1

        return [
            sorted(winners - losers.keys()),
            sorted([loser for loser, losses in losers.items() if losses == 1]),
        ]
