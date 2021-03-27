#include <stdbool.h>
#include <limits.h>

bool isPalindrome(int x)
{
	int	tmp;
	long	reverse_num;
	int	mod_res;

	reverse_num = 0;
	tmp = x;
	if (x < 0 || x > INT_MAX)
		return (false);
	else if (x == 0)
		return (true);
	while (tmp)
	{
		mod_res = tmp % 10;
		reverse_num = reverse_num * 10 + mod_res;
		tmp /= 10;
	}
	if (reverse_num != x || reverse_num > INT_MAX)
		return (false);
	return (true);
}
