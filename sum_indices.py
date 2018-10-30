class Solution(object):
    def sumIndices(self, num_list, target, version):
        """
        :type num_list: List[int]
        :type target: int
        :rtype: int
        """
        if version == 1:
            for idx, value in enumerate(num_list):
                for j in range(idx+1, len(num_list)):
                    if (value + num_list[j]) == target:
                        return [idx, j]
            return [0, 0]

        if version == 2:
            num_set = set(num_list)
            for idx, value in enumerate(num_list):
                if (target - value) in num_set:
                    return [idx, num_list.index(target-value)]
            return [0, 0]

        return 'Version 1 or 2?'
