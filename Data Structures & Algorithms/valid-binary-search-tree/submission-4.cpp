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

    bool isValid(TreeNode* root, int leftLimit, int rightLimit) {
        if (!root) {
            return true;
        }
        if (!(leftLimit < root->val && root->val < rightLimit)) {
            return false;
        }
        return isValid(root->left, leftLimit, root->val) && isValid(root->right, root->val, rightLimit);
    }
 
    bool isValidBST(TreeNode* root) {
        if (!root) {
            return true;
        }
        int leftLimit = -5000;
        int rightLimit = 5000;
        return isValid(root, leftLimit, rightLimit);
    }
};
