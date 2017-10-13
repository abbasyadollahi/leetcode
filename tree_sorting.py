class tree_sorting(object):

    def __init__(self, links, values):
        """
        Initialize your data structure here.
        :type values: list
        :type links: list
        """
        self.links = links
        self.values = values
        self.nodes = len(values)

    def find_longest(self):
        """
        Player {player} makes a move at ({row}, {col}).
        :type row: int
        :rtype: int
        """

        longest = []

        for i in range(1, self.nodes+1):
            first =


