
/*
class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/

class Solution {
  public:
    int height(Node* root) {
        // code here
        if(root==NULL)return -1;
        int op1=height(root->left);
        int op2=height(root->right);
        int ans=max(op1,op2)+1;
        return ans;
    }
};