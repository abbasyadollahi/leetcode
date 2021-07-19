// https://leetcode.com/problems/two-sum/

function twoSum(nums: number[], target: number): number[] {
    let seen = {};
    for (let [index, num] of nums.entries()) {
        if (target - num in seen) {
            return [seen[target - num], index];
        } else {
            seen[num] = index;
        }
    }
};
