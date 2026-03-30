class Solution:

    def conflict(self, s1, s2):
        n = min(len(s1), len(s2))
        for i in range(n):
            if s1[i] != s2[i]:
                return (s1[i], s2[i])
        if len(s1) > len(s2):
            return ("INVALID", "INVALID")
        return None

    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indeg = {char: 0 for word in words for char in word}
        
        for w1, w2 in zip(words, words[1:]):
            res = self.conflict(w1, w2)
            if res == ("INVALID", "INVALID"):
                return ""
            if res:
                c1, c2 = res
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indeg[c2] += 1

        q = deque([node for node in indeg if indeg[node] == 0])

        res = []

        while q:
            u = q.popleft()
            res.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        ret = "".join(res)
        return ret if len(ret) == len(indeg) else ""

        return ""
        