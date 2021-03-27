#include <stdbool.h>
#include <stdio.h>

bool	isPalindrome(int x);

int main()
{
	int x = 1203;
	bool b;
	
	b = isPalindrome(x);
	printf("%d\n", b);
	return (0);
}
