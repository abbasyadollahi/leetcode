# To test the 'Versions' method of *Question B*, I used python's built-in 'unittest' framework.
# There are 20 test cases, covering the most important features of the code.

import sys
import unittest

from .versions import Solution


class QuestionBTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testV1GreaterThanV2(self):
        v1 = '10.0'
        v2 = str(float(v1) / 2)

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is greater than {v2}.')

    def testV1LessThanV2(self):
        v1 = '10.0'
        v2 = str(float(v1) * 2)

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is less than {v2}.')

    def testV1EqualToV2(self):
        v1 = v2 = '10.0'

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} and {v2} are equal versions.')

    def testV2IsInt(self):
        v1 = '10.0'
        v2 = '10'

        self.assertEqual(self.solution.versions(v1, v2), f'10.0 and 10 are equal versions.')

    def testV1IsNegative(self):
        v1 = '-22.0'
        v2 = '19.0'

        self.assertRaises(ValueError, self.solution.versions, v1, v2)

    def testV1IsNone(self):
        v1 = None
        v2 = '10.0'

        self.assertRaises(TypeError, self.solution.versions, v1, v2)

    def testV2IsStringNone(self):
        v1 = '10.0'
        v2 = 'None'

        self.assertRaises(ValueError, self.solution.versions, v1, v2)

    def testV2IsNotString(self):
        v1 = '5.55'
        v2 = 10.0

        self.assertRaises(TypeError, self.solution.versions, v1, v2)

    def testV1V2AreStrings(self):
        v1 = '15.55'
        v2 = '10.0'

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is greater than {v2}.')

    def testV1IsListString(self):
        v1 = ['1.21']
        v2 = '10.0'

        self.assertRaises(TypeError, self.solution.versions, v1, v2)

    def testV1WithManyDecimals(self):
        v1 = '2.123456789'
        v2 = '2.9'

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is greater than {v2}.')

    def testV1LimitEqualV2(self):
        v1 = '2.999999999999999999999999999999999999999'
        v2 = '3'

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is less than {v2}.')

    def testV1WrongPattern(self):
        v1 = '.20.2'
        v2 = '20.1.'

        self.assertRaises(ValueError, self.solution.versions, v1, v2)

    def testV1DoubleDot(self):
        v1 = '20..2'
        v2 = '20.1'

        self.assertRaises(ValueError, self.solution.versions, v1, v2)

    def testV1MultiLevelVersion(self):
        v1 = '20.2.3.4.1.2'
        v2 = '20.1.2'

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is greater than {v2}.')

    def testV1EmptyString(self):
        v1 = ''
        v2 = '20.1'

        self.assertRaises(IndexError, self.solution.versions, v1, v2)

    def testV1MaxInt(self):
        v1 = str(sys.maxsize)
        v2 = '2'

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is greater than {v2}.')

    def testV1IsZero(self):
        v1 = '0.0'
        v2 = '1.0'

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is less than {v2}.')

    def testV1StartsWithMultiZero(self):
        v1 = '00001.2.3.4'
        v2 = '1.1.2'

        self.assertEqual(self.solution.versions(v1, v2), f'{v1} is greater than {v2}.')

    def testV1V2Letters(self):
        v1 = 'a.b.c'
        v2 = 'a.b.d'

        self.assertRaises(ValueError, self.solution.versions, v1, v2)


if __name__ == '__main__':
    unittest.main()
