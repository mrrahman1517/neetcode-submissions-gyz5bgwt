class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjancency list and degree data structures
        graph = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        # lets create a queue
        queue = deque()
        # first push all 0 indegree nodes into queue
        for n in range(numCourses):
            if indeg[n] == 0:
                queue.append(n)
        
        if not queue:
            # no 0 in degree, false
            return False
        count = 0
        while queue:
            u = queue.popleft()
            count += 1
            # pop first 0 deg node
            for v in graph[u]:
                # indeg[v] > 0
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v) 

        return count == numCourses