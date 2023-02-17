# https://leetcode.com/problems/single-threaded-cpu/

import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        time = 1
        order = []

        queue = [(*task, index) for index, task in enumerate(tasks)]
        heapq.heapify(queue)

        available = []
        heapq.heapify(available)

        while len(order) < len(tasks):
            while queue and time >= queue[0][0]:
                _, processing_time, index = heapq.heappop(queue)
                heapq.heappush(available, (processing_time, index))

            if available:
                processing_time, index = heapq.heappop(available)
                time += processing_time
                order.append(index)
            else:
                time = queue[0][0]

        return order

    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        time = 1
        order = []
        available = []
        queue = sorted(((*task, index) for index, task in enumerate(tasks)), reverse=True)

        while len(order) < len(tasks):
            while queue and time >= queue[-1][0]:
                _, processing_time, index = queue.pop()
                heapq.heappush(available, (processing_time, index))

            if available:
                processing_time, index = heapq.heappop(available)
                time += processing_time
                order.append(index)
            else:
                time = queue[-1][0]

        return order
