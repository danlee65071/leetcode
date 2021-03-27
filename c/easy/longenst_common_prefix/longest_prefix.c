#include <stdlib.h>

char * longestCommonPrefix(char ** strs, int strsSize)
{
	char	*prefix;
	int	    i;
	int	    j;
	int	    min_len;
	char	buf;
	int 	check;
    int	    k;

	k = 0;
	min_len = 0;
	check = 1;
	if (strsSize < 1)
		return ("");
	else if (strsSize == 1)
		return (strs[0]);
	j = 0;
	while (strs[0][j])
		j++;
	min_len = j;
	i = 1;
	while (i < strsSize)
	{	
		j = 0;
		while (strs[i][j])
			j++;
		if (min_len > j)
			min_len = j;
		i++;
	}
	j = 0;
	prefix = malloc(sizeof(char) *(min_len + 1));
	while (j < min_len)
	{
		buf = strs[0][j];
		i = 1;
		while (i < strsSize)
		{
			if (strs[i][j] == buf)
				check = 1;
			else
			{
				check = 0;
				break ;
			}
			i++;
		}
		if (check)
			prefix[k++] = buf;
		else 
			break ;
		j++;
	}
	prefix[k] = '\0';
	return (prefix);
}
