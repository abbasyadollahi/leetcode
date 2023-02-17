# https://leetcode.com/problems/minimum-height-trees/

from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        node_connections = defaultdict(set)
        for node, connection in edges:
            node_connections[node].add(connection)
            node_connections[connection].add(node)

        while len(node_connections) > 2:
            leaves = [node for node, connections in node_connections.items() if len(connections) == 1]
            for leaf in leaves:
                connection = node_connections.pop(leaf).pop()
                node_connections[connection].discard(leaf)

        return list(node_connections.keys())

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        node_connections = defaultdict(set)
        for node, connection in edges:
            node_connections[node].add(connection)
            node_connections[connection].add(node)

        leaves = [node for node, connections in node_connections.items() if len(connections) == 1]
        while len(node_connections) > 2:
            new_leaves = []
            for leaf in leaves:
                connection = node_connections.pop(leaf).pop()
                node_connections[connection].discard(leaf)
                if len(node_connections[connection]) == 1:
                    new_leaves.append(connection)
            leaves = new_leaves

        return list(node_connections.keys())
