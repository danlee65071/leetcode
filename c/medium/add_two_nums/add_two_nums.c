#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
 };

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    struct ListNode *begin;
    struct ListNode *current;
    struct ListNode *previous;
    int             n;
    int             a;

    a = 0;
    begin = malloc(sizeof(struct ListNode));
    n = l1->val + l2->val;
    begin->val = n % 10;
    begin->next = NULL;
    if (n >= 10)
        a = 1;
    else
        a = 0;
    previous = begin;
    l1 = l1->next;
    l2 = l2->next;
    while (l1 || l2)
    {
        if (l1 == NULL)
        {
            n = l2->val;
            l2 = l2->next;
        }
        else if (l2 == NULL)
        {
            n = l1->val;
            l1 = l1->next;
        }
        else
        {
            n = l1->val + l2->val;
            l1 = l1->next;
            l2 = l2->next;
        }
        n += a;
        if (n >= 10)
            a = 1;
        else
            a = 0;
        current = malloc(sizeof(struct ListNode));
        current->val = n % 10;
        current->next = NULL;
        previous->next = current;
        previous = current;
    }
    if (a != 0)
    {
            current = malloc(sizeof(struct ListNode));
            current->val = a;
            previous->next = current;
            current->next = NULL;
    }
    return (begin);
}
