#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize);

int main()
{
	int nums[] = {3, 3};
	int target = 6;
	int returnSize = 2;
	int *ptr;

	ptr = 0;
	ptr = twoSum(nums, 2, target, &returnSize);
	printf("[%d, %d]\n", ptr[0], ptr[1]);
	free(ptr);
	return (0);
}
