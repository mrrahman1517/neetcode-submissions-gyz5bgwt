class PrefixNode {
public:
    map<char, PrefixNode*> children;
    bool endWord;
    PrefixNode() {
        endWord = false;
    }
};

class PrefixTree {
    PrefixNode* root;
public:
    PrefixTree() {
        root = new PrefixNode();
    }
    
    void insert(string word) {
        PrefixNode *curr = root;
        for (auto & ch: word) {
            if (!curr->children.count(ch)) {
                curr->children[ch] = new PrefixNode();
            }
            curr = curr->children[ch];
        }
        curr->endWord = true;
    }
    
    bool search(string word) {
        PrefixNode *curr = root;
        for (auto & ch: word) {
            if(!curr->children.count(ch)) {
                return false;
            }
            curr = curr->children[ch];
        }
        return curr->endWord;
    }
    
    bool startsWith(string prefix) {
        PrefixNode *curr = root;
        for (auto & ch: prefix) {
            if(!curr->children.count(ch)) {
                return false;
            }
            curr = curr->children[ch];
        }
        return true;
    }
};
