# https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        max_age = max(ages)
        max_score = max(scores)
        players = sorted(zip(ages, scores))
        dp = [[0] * (max_score + 1) for _ in range(max_age + 1)]

        i = 0
        for age in range(1, len(dp)):
            for score in range(1, len(dp[0])):
                while i < len(players) and players[i][0] <= age and players[i][1] <= score:
                    dp[age][score] += players[i][1]
                    i += 1
                dp[age][score] = max(dp[age][score] + dp[age-1][score], dp[age][score] + dp[age][score-1])

        return dp[-1][-1]

    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        players = sorted(zip(ages, scores))
        dp = [score for _, score in players]

        for i, (_, score) in enumerate(players):
            for j in range(i):
                if players[j][1] <= score:
                    dp[i] = max(dp[i], dp[j] + score)

        return max(dp)
