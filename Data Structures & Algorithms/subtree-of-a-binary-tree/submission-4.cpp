/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:

    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr and q == nullptr) {
            return true;
        }
        if (p == nullptr and q != nullptr) {
            return false;
        }
        if (p != nullptr and q == nullptr) {
            return false;
        }
        if (p->val != q->val) {
            return false;
        }
        return isSameTree(p->left, q->left) and isSameTree(p->right, q->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr and subRoot == nullptr) {
            return true;
        }    
        bool firstTest = isSameTree(root, subRoot);
        if (firstTest) {
            return true;
        }
        bool leftResult = false;
        if (root->left != nullptr) {
            leftResult = isSubtree(root->left, subRoot);
        }
        bool rightResult = false;
        if (root->right != nullptr) {
            rightResult = isSubtree(root->right, subRoot);
        }
        if (leftResult or rightResult) {
            return true;
        }
    }
};
