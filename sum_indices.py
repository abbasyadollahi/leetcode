class Solution:
    def sumIndicesV1(self, num_list, target):
        """
        :type num_list: List[int]
        :type target: int
        :rtype: List[int]
        """

        for idx, value in enumerate(num_list):
            for j in range(idx+1, len(num_list)):
                if (value + num_list[j]) == target:
                    return [idx, j]
        return [0, 0]

    def sumIndicesV2(self, num_list, target):
        """
        :type num_list: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_set = set(num_list)
        for idx, value in enumerate(num_list):
            if (target - value) in num_set:
                return [idx, num_list.index(target-value)]
        return [0, 0]
