# https://leetcode.com/problems/course-schedule/

from typing import List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Course i is prereq for courses in graph[i]
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        done = [False] * numCourses
        for course in range(numCourses):
            if not done[course]:
                if self.cyclic(course, done, set(), graph):
                    return False
        return True

    def cyclic(self, course: int, done: List[bool], seen: Set[int], graph: List[List[int]]) -> bool:
        if course in seen:
            seen.remove(course)
            return True
        elif done[course]:
            return False
        else:
            done[course] = True
            seen.add(course)

        for dep in graph[course]:
            if self.cyclic(dep, done, seen, graph):
                return True
        seen.remove(course)
        return False
