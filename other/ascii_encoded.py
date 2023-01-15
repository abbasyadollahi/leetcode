class Solution:
    def decode(self, encoded: str) -> str:
        space = 32
        uppercase = list(range(65, 91))
        lowercase = list(range(97, 123))
        characters = {space, *uppercase, *lowercase}

        code = ''
        message = ''
        for digit in encoded[::-1]:
            code += digit
            int_code = int(code)

            if int_code in characters:
                message += chr(int_code)
                code = ''

        return message


sol = Solution()
assert sol.decode('511011501782351112179911801562340161171141148') == 'Truth Always Wins'
