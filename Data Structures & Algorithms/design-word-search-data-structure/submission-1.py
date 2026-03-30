class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j, len(word)):
                if word[i] =='.':
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    return dfs(i + 1, node.children[word[i]])
            return node.endOfWord
            
        return dfs(0, self.root)        
