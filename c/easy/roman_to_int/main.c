#include <stdio.h>

int romanToInt(char *s);

int main()
{
	char	s[] = "LVIII";
	int	res = 0;

	res = romanToInt(s);
	printf("%d\n", res);
	return (0);
}
