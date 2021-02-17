# The 'Overlap' method takes in two arguments, each being a tuple of two numbers, and returns
# whether there's an overlap between the two ranges. If either of the input arguments are
# invalid, the method will raise an appropriate exception.

from typing import Tuple, Union


# Custom Typing
Number = Union[int, float]
Coords = Tuple[Number, Number]


class Solution:
    def overlap(self, l1: Coords, l2: Coords) -> bool:
        """
        :type l1: tuple - Coordinates of start/end points on line
        :type l2: tuple - Coordinates of start/end points on line
        :rtype: bool - True if both lines overlap
        """
        if isinstance(l1, (list, tuple)) and len(l1) == 2:
            try:
                x1, x2 = map(float, l1)
            except:
                raise TypeError('Both elements in l1 must be a number (or a string representation of a number).')
        else:
            raise TypeError('Argument l1 must be a list or tuple of numbers of size 2.')

        if isinstance(l2, (list, tuple)) and len(l2) == 2:
            try:
                x3, x4 = map(float, l1)
            except:
                raise TypeError('Both elements in l2 must be a number (or a string representation of a number).')
        else:
            raise TypeError('Argument l2 must be a list or tuple of numbers of size 2.')

        return x1 <= x4 and x2 >= x3

sol = Solution()
print(sol.overlap((1,5), (4,6)))
print(sol.overlap((1,10), (4,6)))
print(sol.overlap((1,3.9), (4,6)))
print(sol.overlap((1,5), (6,7)))

print(sol.overlap((7,5), (4,6)))
print(sol.overlap((7,5), (6,4)))

print(sol.overlap((7,5,3), (6,4)))
print(sol.overlap(None, None))
print(sol.overlap((None, None), None))
print(sol.overlap((None, None), (None, None)))
