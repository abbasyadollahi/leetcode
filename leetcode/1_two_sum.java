// https://leetcode.com/problems/two-sum/

package leetcode;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        int i;
        for (i = 0; i < nums.length; i++) {
            if (seen.containsKey(target - nums[i])) {
                break;
            }
            seen.put(nums[i], i);
        }

        return new int[] {seen.get(target - nums[i]), i};
    }
}
