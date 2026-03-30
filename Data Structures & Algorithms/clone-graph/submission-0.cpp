/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    map<Node*, Node*> old_to_new;
    Node* copy(Node* old) {
        if (old_to_new.find(old) != old_to_new.end()) {
            // clone exists
            return old_to_new[old];
        }
        Node* newNode = new Node(old->val);
        old_to_new[old] = newNode;
        for (auto* neighbor: old->neighbors) {
            newNode->neighbors.push_back(copy(neighbor));
        }
        return newNode;
    }
    Node* cloneGraph(Node* node) {
        if (!node) {
            return NULL;
        }
        return copy(node);
    }
};
