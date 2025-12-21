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
pair<bool,int>BalanceFast(TreeNode* root){
    if(root==NULL){
         pair<bool,int>p=make_pair(true,0);
        return p;
    }
    pair<bool,int>leftans=BalanceFast(root->left);
    pair<bool,int>rightans=BalanceFast(root->right);

    bool left=leftans.first;
    bool right=rightans.first;
    bool diff= abs(leftans.second-rightans.second)<=1;

    pair<bool,int>ans;
    ans.second=max(leftans.second,rightans.second)+1;
    if(left && right && diff)ans.first=true;
    else ans.first=false;
    return ans;
}
    bool isBalanced(TreeNode* root) {
        return BalanceFast(root).first;
    }
};