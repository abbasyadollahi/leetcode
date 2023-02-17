# https://leetcode.com/problems/course-schedule/

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Course i is prerequisite for courses in graph[i]
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        done = [False] * numCourses
        def cyclic(course: int, seen: set[int]) -> bool:
            if course in seen:
                seen.remove(course)
                return True
            elif done[course]:
                return False
            else:
                done[course] = True
                seen.add(course)

            for dep in graph[course]:
                if cyclic(dep, seen):
                    return True
            seen.remove(course)
            return False

        for course in range(numCourses):
            if not done[course]:
                if cyclic(course, set()):
                    return False
        return True

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_prerequisites = defaultdict(set)
        for course, prerequisite in prerequisites:
            course_prerequisites[course].add(prerequisite)

        visited = [False] * numCourses
        def cyclic(course: int, seen: set[int]) -> bool:
            if visited[course]:
                return False
            if course in seen:
                return True

            seen.add(course)
            if course in course_prerequisites and any(
                cyclic(prerequisite, seen)
                for prerequisite in course_prerequisites[course]
            ):
                return True
            else:
                seen.remove(course)
                visited[course] = True
                return False

        return not any(cyclic(course, set()) for course in course_prerequisites)
