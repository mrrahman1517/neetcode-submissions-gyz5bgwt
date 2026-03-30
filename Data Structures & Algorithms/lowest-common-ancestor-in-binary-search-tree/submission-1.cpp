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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // if p->val < root <  q->val, p must be in left substree and q in right subtree, so root is the LCA
        // if both p and q are greater than root, search in the right subtree
        // if both p and q are lower than root, search in the left subtree 
        // if one of them is the root, then it has to be the lca
        if (root == p || root == q) {
            return root;
        }
        if (p->val < root->val && root->val < q->val) {
            return root;
        }
        if (q->val < root->val && root->val < p->val) {
            return root;
        }
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }

    }
};
