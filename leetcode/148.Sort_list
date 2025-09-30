/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    private:
   ListNode*  findMid(ListNode* head){
   ListNode*  slow=head;
  ListNode*  fast=head->next;
    while(fast!=NULL && fast->next !=NULL){
        slow=slow->next;
        fast=fast->next->next;
    }
    return slow;
}

ListNode*  merge(ListNode* down,ListNode* right){
    if(down==NULL)return right;
    if(right==NULL)return down;
    ListNode*  ans=new ListNode (-1);
    ListNode*  temp=ans;
    while(down!=NULL && right!=NULL){
        if(down->val<right->val){
temp->next=down;
temp=down;
down=down->next;
        }
        else{
            temp->next=right;
temp=right;
right=right->next;
        }
    }
    while(down!=NULL){
        temp->next=down;
temp=down;
down=down->next;
    }
    while(right!=NULL){
         temp->next=right;
temp=right;
right=right->next;
    }
    ans=ans->next;
    return ans;
}
public:
    ListNode* sortList(ListNode* head) {
         if(head==NULL || head->next==NULL)return head;
    ListNode* mid=findMid(head);
    ListNode* down=head;
   ListNode* right=mid->next;
    mid->next=NULL;
    down=sortList(down);
right=sortList(right);
ListNode* result=merge(down,right);
return result;
    }
};