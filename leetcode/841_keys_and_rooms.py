# https://leetcode.com/problems/keys-and-rooms/

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num_rooms = len(rooms)
        to_visit = [0]
        visited = [False] * num_rooms
        visited_count = 0

        while to_visit:
            room = to_visit.pop()
            keys = [key for key in rooms[room] if not visited[room]]
            to_visit.extend(keys)
            if not visited[room]:
                visited[room] = True
                visited_count += 1
                if visited_count == num_rooms:
                    return True

        return False
