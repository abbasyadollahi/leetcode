# https://leetcode.com/problems/valid-number/

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(
            r"([+-](?=\d|\.))?[0-9]*(((?<=\d)\.)|(\.(?=\d)))?((?<=\.)[0-9]+)?((?<=\d|\.)[eE](?=.)[+-]?[0-9]+)?"
        )
        return bool(pattern.fullmatch(s))
