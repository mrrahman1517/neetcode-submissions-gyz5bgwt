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
    int maxDepth(TreeNode* root) {
       if (root == nullptr) {
            return 0;
       } 
       int maxSubPath = 0;
       if (root->left) {
            maxSubPath = maxDepth(root->left); 
       }
       if (root->right) {
            maxSubPath = max(maxSubPath, maxDepth(root->right));
       }
       return maxSubPath + 1;
    }
};
