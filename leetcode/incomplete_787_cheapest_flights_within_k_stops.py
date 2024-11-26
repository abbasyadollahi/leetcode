# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        connections = defaultdict(list)
        for source, destination, price in flights:
            connections[source].append((destination, price))

        prices = [float("inf")] * n
        prices[src] = 0

        queue = [(src, 0)]
        for _ in range(k + 1):
            next_queue = []
            while queue:
                source, source_price = queue.pop()
                for destination, destination_price in connections[source]:
                    if source_price + destination_price < prices[destination]:
                        prices[destination] = source_price + destination_price
                        next_queue.append((destination, prices[destination]))
            queue = next_queue

        if prices[dst] < float("inf"):
            return prices[dst]
        else:
            return -1
