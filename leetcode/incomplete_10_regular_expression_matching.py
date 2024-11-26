# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i_p = 0

        pp = p + " "
        continuous = ""
        regex_groups = []
        while i_p < len(p):
            if pp[i_p + 1] == "*":
                if continuous:
                    regex_groups.append([continuous, False])
                    continuous = ""
                regex_groups.append([p[i_p], True])
                i_p += 2
            else:
                continuous += p[i_p]
                i_p += 1

        if continuous:
            regex_groups.append([continuous, False])
