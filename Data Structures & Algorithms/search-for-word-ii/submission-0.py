class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])

        root = TrieNode()
        # build trie of the words
        for word in words:
            root.add(word)
        
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or board[r][c] not in node.children):
                return
            
            node = node.children[board[r][c]]
            visited.add((r, c))
            word += board[r][c]

            if node.end:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            visited.remove((r, c))


        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(res)