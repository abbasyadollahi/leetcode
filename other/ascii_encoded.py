class Solution:
    def decode(self, encoded):
        """
        :type encoded: String
        :rtype: String
        """

        if not encoded:
            return ''

        space = 32
        a_z = range(97, 123)
        A_Z = range(65, 91)

        code = ''
        msg = ''
        for digit in encoded[::-1]:
            code += digit
            int_code = int(code)

            if int_code == space:
                msg += ' '
                code = ''
            elif int_code in a_z:
                msg += chr(int_code)
                code = ''
            elif int_code in A_Z:
                msg += chr(int(int_code))
                code = ''

        return msg

sol = Solution()
print(sol.decode('23511011501782351112179911801562340161171141148'))
