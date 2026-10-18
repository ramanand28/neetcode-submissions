from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        # Build graph: prerequisite -> course
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque()

        # Add courses with no prerequisites
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        finish = 0

        while q:
            course = q.popleft()
            finish += 1

            # Reduce indegree of courses dependent on this course
            for nei in adj[course]:
                indegree[nei] -= 1

                # All prerequisites completed
                if indegree[nei] == 0:
                    q.append(nei)

        # True if all courses can be completed
        return finish == numCourses