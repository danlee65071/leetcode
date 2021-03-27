#include <limits.h>

int	reverse(int x)
{
	int	res_mod;
	long	n;

	n = 0;
	while(x)
	{
		res_mod = x % 10;
		n = n * 10 + res_mod;
		x /= 10;	
	}
	if (n < INT_MIN || n > INT_MAX)
		n = 0;
	return (n);
}
