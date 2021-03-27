#include <stdio.h>

char * longestCommonPrefix(char ** strs, int strsSize);

int main()
{
	char *strs[] = {"cir", "car"};

	printf("%s\n", longestCommonPrefix(strs, 2));
	return(0);
}
