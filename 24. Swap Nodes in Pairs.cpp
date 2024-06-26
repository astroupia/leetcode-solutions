class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode* left = head;
        ListNode* curr = head->next;
        ListNode* head1 = curr;
        while(curr != NULL ) {
            if(curr->next == NULL)
            {
                curr->next = left;
                left->next = NULL;
                return head1;
            }
            ListNode* right = curr->next;
            curr->next = left;
            if(right->next!= NULL)
            {left->next = right->next;}
            else
            left->next = right;
            left = right;
            curr = right->next;
        }
        return head1;
        
    }
};