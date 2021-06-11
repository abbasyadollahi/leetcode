# https://leetcode.com/problems/clone-graph/

from typing import Dict, List


class GraphNode:
    def __init__(self, val: int = 0, neighbors: List['GraphNode'] = None):
        self.val = val
        self.neighbors = neighbors or []

class Solution:
    def cloneGraph(self, node: 'GraphNode') -> 'GraphNode':
        if not node:
            return None
        return self.traverse(node, {})

    def traverse(self, node: 'GraphNode', seen: Dict[int, 'GraphNode']) -> 'GraphNode':
        new_node = GraphNode(node.val)
        seen[new_node.val] = new_node

        for neighbor in node.neighbors:
            if neighbor.val in seen:
                new_node.neighbors.append(seen[neighbor.val])
            else:
                new_neighbor = self.traverse(neighbor, seen)
                new_node.neighbors.append(new_neighbor)
        return new_node
