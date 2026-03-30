class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * numCourses
        
        # construct DAG from input

        for (u, v) in prerequisites:
            graph[v].append(u)
            indeg[u] += 1
        
        q = deque([node for node in range(numCourses) if indeg[node] == 0])
        #for node in range(numCourses):
        #    if indeg[node] == 0:
        count = 0
        while q:
            u = q.popleft()
            count += 1
            for v in graph[u]:
                indeg[v] -= 1 # edge (uv) implies indeg(v) > 0
                if indeg[v] == 0:
                    q.append(v)


        return count == numCourses