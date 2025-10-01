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
   ListNode * findMid(ListNode * head){
      ListNode * fast=head->next;
       ListNode * slow=head;
        while(fast!=NULL && fast->next!=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }
        return slow;
    }
    ListNode * reverse(ListNode * head){
        ListNode * curr=head;
        ListNode * prev=NULL;
        ListNode * Next=NULL;
        while(curr!=NULL){
            Next=curr->next;
            curr->next=prev;
            prev=curr;
            curr=Next;
        }
        return prev;
    }
public:
    bool isPalindrome(ListNode* head) {
        if(head==NULL || head->next==NULL) return true;
        ListNode * middle=findMid(head);
        ListNode * temp=middle->next;
        middle->next=reverse(middle->next);
        ListNode *temp1=head;
        ListNode *temp2=middle->next;
        while(temp2!=NULL){
            if(temp1->val !=temp2->val){
                return false;
            }
            temp1=temp1->next;
            temp2=temp2->next;
        }
        return true;
    }
};