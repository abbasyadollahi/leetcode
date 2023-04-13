# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        count = 0
        letter = chars[0]
        for char in chars:
            if char == letter:
                count += 1
            else:
                chars[i] = letter
                letter = char
                i += 1

                if count > 1:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                    count = 1

        chars[i] = letter
        i += 1

        if count > 1:
            for digit in str(count):
                chars[i] = digit
                i += 1

        chars[i:] = []
        return len(chars)
