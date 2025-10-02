/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA==NULL || headB==NULL)return NULL;
        ListNode * pa=headA;
        ListNode * pb=headB;
        while(pa!=pb){
            if(pa!=NULL)pa=pa->next;
            else pa=headB;
            if(pb!=NULL)pb=pb->next;
            else pb=headA;
        }
        return pa;
    }
};