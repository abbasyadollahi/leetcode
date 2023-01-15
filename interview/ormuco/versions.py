# The 'Versions' method takes in two arguments, each being a string representation of a package
# version number with the format '##.##.##.##'. If either of the input arguments are invalid,
# the method will raise an appropriate exception. Otherwise, it will compare the version and
# return whether version 1 is greater, equal or less than version 2.
# During the implementation, I assumed that bigger numbers are greater (i.e. '1.1119' is greater
# than '1.9'). I also assumed that versions with more subversions are greater (i.e. '1.2.3.4' is
# greater than '1.2' but less than '1.3'), except when all subversions, that the other version
# doesn't have, are '0' (i.e. '1.2.0.0.0' is equal to '1.2.0').

import re


class Solution:
    def versions(self, v1: str, v2: str) -> str:
        """
        :param v1: Version number 1
        :param v2: Version number 2
        :return: Message comparing version 1 and version 2
        """
        regex = re.compile('^((\d+)?)$|^(((\d+)\.)+(\d+))$')

        if not all([isinstance(v, str) for v in (v1, v2)]):
            raise TypeError('Arguments v1 and v2 must be string representations of a version number.')
        elif len(v1) == 0 or len(v2) == 0:
            raise IndexError('Arguments v1 and v2 must at least be of length 1.')
        elif not regex.match(v1) or not regex.match(v2):
            raise ValueError('Arguments v1 and v2 must follow the following pattern: 1.0.12.00.123 (no dot at start/end).')

        v1_multi = list(filter(None, v1.split('.')))
        v2_multi = list(filter(None, v2.split('.')))
        diff = len(v1_multi) - len(v2_multi)

        if diff > 0:
            v2_multi += ['0'] * diff
        elif diff < 0:
            v1_multi += ['0'] * abs(diff)

        for n1, n2 in zip(v1_multi, v2_multi):
            if n1.lstrip('0') != n2.lstrip('0'):
                return f'{v1} is {"greater" if float(n1) > float(n2) else "less"} than {v2}.'

        return f'{v1} and {v2} are equal versions.'
