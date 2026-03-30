class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(u):
            if visited[u]:
                return
            else:
                visited[u] = 1
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)

        graph = defaultdict(list)
        visited = [0] * n
        # build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # now run dfs for every node, each dfs is a component
        count = 0
        for node in range(n):
            if not visited[node]:
                count += 1
                dfs(node)
        return count
        
        
        