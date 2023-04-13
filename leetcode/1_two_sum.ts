// https://leetcode.com/problems/two-sum/

function twoSum(nums: number[], target: number): number[] {
    let seen = {};

    let num, i;
    for ([i, num] of nums.entries()) {
        if (target - num in seen) {
            break;
        }
        seen[num] = i;
    }

    return [seen[target - num], i];
};
