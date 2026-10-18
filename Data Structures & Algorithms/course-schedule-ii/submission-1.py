from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        # Build graph: prerequisite -> course
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque()

        # Add courses that have no prerequisites
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        output = []

        while q:
            course = q.popleft()
            output.append(course)

            # Reduce indegree of dependent courses
            for nei in adj[course]:
                indegree[nei] -= 1

                # All prerequisites completed
                if indegree[nei] == 0:
                    q.append(nei)

        # If all courses are completed, return order
        if len(output) == numCourses:
            return output

        return []