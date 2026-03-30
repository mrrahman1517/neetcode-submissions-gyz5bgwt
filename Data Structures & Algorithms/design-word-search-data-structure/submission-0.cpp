class PrefixNode {
public:
    map<char, PrefixNode*> children;
    bool endWord;
    PrefixNode() {
        children = map<char, PrefixNode*>();
        endWord = false;
    }
};

class WordDictionary {
public:
    PrefixNode* root;
    WordDictionary() {
        root = new PrefixNode();
    }
    
    void addWord(string word) {
        PrefixNode* curr = root;
        for (auto& c: word) {
            if (curr->children.find(c) == curr->children.end()) {
                curr->children[c] = new PrefixNode();
            }
            curr = curr->children[c];
        }
        curr->endWord = true;
    }

    bool dfs (PrefixNode* root, int i, string word) {
        PrefixNode* curr = root;
        for (; i < word.size(); i++) {
            if (word[i] == '.') {
                for (auto& child: curr->children) {
                    if (dfs(child.second, i+1, word)) {
                        return true;
                    }
                }
                return false;
            }
            else {
                if (curr->children.find(word[i]) == curr->children.end()) {
                    return false;
                }
                else {
                    curr = curr->children[word[i]];
                }
            }
        }
        return curr->endWord;
    }
    
    bool search(string word) {
        return dfs(root, 0, word);
    }
};
