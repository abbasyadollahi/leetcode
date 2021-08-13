from typing import List


class Solution:
    def prime_permutations(self, num: int) -> List[int]:
        digits = self.digitize(num)
        perms = self.permutations(digits)
        primes = list(filter(self.is_prime, perms))
        return list(set(primes))

    def digitize(self, num: int) -> List[int]:
        digits = []
        tmp_num = num
        while tmp_num != 0:
            digits.append(tmp_num % 10)
            tmp_num //= 10
        return digits[::-1]

    def numerize(self, digits: List[int]) -> int:
        num = 0
        for digit in digits:
            num *= 10
            num += digit
        return num

    def permutations(self, digits: List[int]) -> List[int]:
        perms = []

        def permute(perm: List[int], choices: List[int]) -> None:
            for i, choice in enumerate(choices):
                permute([*perm, choice], [*choices[:i], *choices[i+1:]])
            if not choices:
                perms.append(self.numerize(perm))

        permute([], digits)
        return perms

    def is_prime(self, num: int) -> bool:
        return next((False for mod in range(2, num) if num % mod == 0), True)


sol = Solution()
print(sol.prime_permutations(133))
