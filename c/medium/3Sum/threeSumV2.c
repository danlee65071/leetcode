#include <stdlib.h>

int comp (const int *arg1, const int *arg2)
{
return *arg1 - *arg2;
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{
    int total = 64;
    int **res = malloc(sizeof(int*) * total);
    int target_ind, i, j, tmp;

    if (numsSize < 3)
    {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    qsort(nums, numsSize, sizeof(int), (int(*) (const void *, const void *)) comp);
    *returnSize = 0;
    (*returnColumnSizes) = malloc(sizeof(int) * total);
    for (target_ind = 0; target_ind < numsSize; target_ind++)
    {
        if (target_ind > 0 && nums[target_ind] == nums[target_ind - 1])
            continue;
        j = numsSize - 1;
        i = target_ind + 1;
        while(i < j)
        {
            tmp = nums[target_ind] + nums[i] + nums[j];
            if (tmp < 0)
                i++;
            else if (tmp > 0)
                j--;
            else
            {
                (*returnSize)++;
                res[*returnSize - 1] = malloc(sizeof(int) * 3);
                res[*returnSize - 1][0] = nums[target_ind];
                res[*returnSize - 1][1] = nums[i++];
                res[*returnSize - 1][2] = nums[j--];
                (*returnColumnSizes)[*returnSize - 1] = 3;
                while (i < j && nums[i] == nums[i - 1])
                    i++;
                while (i < j && nums[j] == nums[j - 1])
                    j--;
                if((*returnSize) == total)
                {
                    total *= 2;
                    *returnColumnSizes=(int*)realloc(*returnColumnSizes, sizeof(int)*total);
                    res = realloc(res, sizeof(int*)*total);
                }
            }
        }
    }
    return res;
}
