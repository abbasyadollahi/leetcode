# https://leetcode.com/problems/elimination-game/


class Solution:
    def lastRemaining(self, n: int) -> int:
        nums = list(range(n))

        left_to_right = True
        while len(nums) > 1:
            nums = nums[1 if left_to_right else len(nums) % 2 :: 2]
            left_to_right = not left_to_right

        return nums.pop() + 1

    def lastRemaining(self, n: int) -> int:
        step = 1
        head = 1
        left_to_right = True

        while n > 1:
            if left_to_right:
                head += step
            else:
                head += (n % 2) * step
            n //= 2
            step *= 2
            left_to_right = not left_to_right

        return head
