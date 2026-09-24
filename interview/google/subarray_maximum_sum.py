def find_sum(nums: list[int]) -> tuple[int, int]:
    running_sum = 0
    running_sums = [running_sum := running_sum + num for num in nums]

    prefix_sums = {num: [i, i, 2 * num] for i, num in enumerate(reversed(nums))}

    for i, num in enumerate(nums):
        old_running
        if
        prefix_sums[]



assert find_sum([1, 3, 5, 6, 3, -6, 3]) == (1, 4)
