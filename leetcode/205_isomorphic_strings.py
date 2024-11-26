# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings_s = {}
        mappings_t = {}
        for ss, tt in zip(s, t):
            print(ss, tt, mappings_s, mappings_t)
            if ss in mappings_s or tt in mappings_t:
                if mappings_s[ss] != tt or mappings_t[tt] != ss:
                    return False
            else:
                mappings_s[ss] = tt
                mappings_t[tt] = ss
        return True
