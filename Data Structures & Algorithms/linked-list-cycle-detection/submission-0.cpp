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
    bool hasCycle(ListNode* head) {
        unordered_set<ListNode*> duplicate;
        ListNode* ptr = head;
        while(ptr) {
            if (duplicate.find(ptr) != duplicate.end()) {
                return true;
            }
            duplicate.insert(ptr);
            ptr = ptr->next;
        }
        return false;
    }
};
