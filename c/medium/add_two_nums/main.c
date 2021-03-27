#include <stdio.h>

struct ListNode
{
     int val;
     struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2);

int main()
{
	struct ListNode *l1;
	struct ListNode	el1;
	struct ListNode el2;
	struct ListNode el3;
	struct ListNode	*l2;
	struct ListNode el4;
	struct ListNode el5;
	struct ListNode el6;
	struct ListNode	*res;

	l1 = &el1;
	el1.val = 2;
	el1.next = &el2;
	el2.val = 4;
	el2.next = &el3;
	el3.val = 3;
	el3.next = NULL;
	
	l2 = &el4;
	el4.val = 5;
	el4.next = &el5;
	el5.val = 6;
	el5.next = &el6;
	el6.val = 4;
	el6.next = NULL;
	
	res = addTwoNumbers(l1, l2);
	
	while (res)
	{
		printf("%d ", res->val);
		res = res->next;
	}
	printf("\n");
	return (0);
}
