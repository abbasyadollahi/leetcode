class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        count = 0

        for i in range(1, n+1):
            if i < 10:
                digit += 1
                count += 1

                if n == count:
                    return digit
            else:
                number = str(i)
                num_len = len(number)

                for x in range(num_len):
                    digit = number[x]
                    count += 1

                    if n == count:
                        return digit


