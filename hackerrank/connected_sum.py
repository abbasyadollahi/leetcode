# https://www.hackerrank.com/x/library/hackerrank/all/questions/932081/view

import math
from typing import List


def connectedSum(graph_nodes: int, graph_from: List[int], graph_to: List[int]) -> int:
    edges = [[] for _ in range(graph_nodes + 1)]
    for from_node, to_node in zip(graph_from, graph_to):
        edges[from_node].append(to_node)
        edges[to_node].append(from_node)

    sizes = []
    seen = [False] * (graph_nodes + 1)
    for node in range(1, graph_nodes + 1):
        if seen[node] is False:
            seen[node] = True
            sizes.append(graph_size(node, edges, seen))

    return sum(map(math.ceil, map(math.sqrt, sizes)))

def graph_size(node: int, edges: List[List[int]], seen: List[bool]) -> int:
    size = 1
    nodes = edges[node]
    while nodes:
        n = nodes.pop()
        if seen[n] is False:
            size += 1
            seen[n] = True
            nodes.extend(edges[n])

    return size
