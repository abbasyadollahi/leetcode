# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s
        elif num_rows == 2:
            return s[::2] + s[1::2]

        i = 0
        forward = True
        rows = [[] for i in range(num_rows)]
        for c in s:
            rows[i].append(c)
            if forward:
                if i == num_rows - 1:
                    i -= 1
                    forward = False
                else:
                    i += 1
            else:
                if i == 0:
                    i += 1
                    forward = True
                else:
                    i -= 1

        return ''.join(''.join(r) for r in rows)


sol = Solution()
print(sol.convert('ABCD', 3))
print(sol.convert('PAYPALISHIRING', 3))
print(sol.convert('ABCDEFGHIJKLMNOPQRS', 5))
