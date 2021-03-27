#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
	int	i;
	int	j;
	int	*res;

	i = 0;
	res = 0;
	while (i < numsSize - 1)
	{
		j = i + 1;
		while (j < numsSize)
		{
			if (nums[i] + nums[j] == target)
			{
				*returnSize = 2;
				res = malloc(sizeof(int) * *returnSize);
				res[0] = i;
				res[1] = j;
				return (res);
			}
			j++;
		}
		i++;
	}
	*returnSize = 0;
	res = 0;
	return (res);
}
