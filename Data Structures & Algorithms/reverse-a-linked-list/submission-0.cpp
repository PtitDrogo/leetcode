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
public:
    ListNode* reverseList(ListNode* head) 
    {
        ListNode *it = head;
        int size = 0;
        if (head == NULL)
            return NULL;
        while (it->next)
        {
            it = it->next;
            size++;
        }
        // printf("%i\n", size);
        ListNode *currFNode = it;
        ListNode *RESULT = it;

        while (size >= 0)
        {
            it = head;
            for (int i = 0; i < size; i++)
                it = it->next;
            currFNode->next = it;
            currFNode = it;
            size--;
            printf("%i\n", size);
        }
        currFNode->next = NULL;
        return RESULT;
    }
};
