class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        p = [x for x in range(n)]
        sz = [1 for _ in range(n)]
        self.count = n
        # use edge and disjoint set data structure
        def find(x):
            while x != p[x]:
                p[x] = p[p[x]]
                x = p[x]
            return x
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return
            self.count -= 1
            if sz[pu] <= sz[pv]:
                # pu smaller tree, make parent(pu) = pv
                p[pu] = pv
                sz[pv] += sz[pu]
            else:
                p[pv] = pu
                sz[pu] += sz[pv]
        for (u, v) in edges:
            union(u, v)
        return self.count == 1