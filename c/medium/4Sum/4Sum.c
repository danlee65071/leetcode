#include <stdlib.h>
#include <stdio.h>


int comp (const int *arg1, const int *arg2);
int **two_sum(int *nums, int numsSize, int target, int *returnSize);
void k_sum(int *nums, int numsSize, int target, int k, int *returnSizeTwoSum, int *returnSize, int **res, int ***resTwoSum, int *prevReturnSize);

int g_res_malloc = 64;

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes)
{
    int **res = NULL;
    int **resTwoSum = NULL;
    int returnSizeTwoSum = 0;
    int k = 4;
    int prevReturnSize = 0;

    *returnSize = 0;
    qsort(nums, numsSize, sizeof(int), (int (*)(const void *, const void *)) comp);
    res = malloc(sizeof(int *) * g_res_malloc);
    for (int i = 0; i < g_res_malloc; i++)
    {
        res[i] = malloc(sizeof(int) * 4);
    }
    k_sum(nums, numsSize, target, k, &returnSizeTwoSum, returnSize, res, &resTwoSum, &prevReturnSize);
    (*returnColumnSizes) = malloc(sizeof(int) * *returnSize);
    for (int i = 0; i < *returnSize; i++)
    {
        (*returnColumnSizes)[i] = 4;
    }
    return res;
}

void k_sum(int *nums, int numsSize, int target, int k, int *returnSizeTwoSum, int *returnSize, int **res, int ***resTwoSum, int *prevReturnSize)
{
    if ((numsSize == 0) || (*nums * k > target) || (*(nums + numsSize - 1) * k < target))
    {
        return;
    }
    if (k == 2)
    {
        *resTwoSum = two_sum(nums, numsSize, target, returnSizeTwoSum);
        return;
    }
    for (int i = 0; i < numsSize; i++)
    {
        if (i == 0 || nums[i] != nums[i - 1])
        {
            if (*returnSize >= g_res_malloc)
            {
                g_res_malloc *= 2;
                res = realloc(res, sizeof(int *) * g_res_malloc);
                for (int i = *returnSize; i < g_res_malloc; i++)
                {
                    res[i] = malloc(sizeof(int) * 4);
                }
            }
            k_sum(nums + i + 1, numsSize - i - 1, target - nums[i], k - 1, returnSizeTwoSum, returnSize, res, resTwoSum, prevReturnSize);
            if (k != 4)
            {
                for (int j = 0; j < *returnSizeTwoSum; j++)
                {
                    res[*returnSize][1] = nums[i];
                    res[*returnSize][2] = (*resTwoSum)[j][0];
                    res[*returnSize][3] = (*resTwoSum)[j][1];
                    (*returnSize)++;
                }
                for (int j = 0; j < *returnSizeTwoSum; j++)
                {
                    free((*resTwoSum)[j]);
                }
                if (*returnSizeTwoSum != 0)
                {
                    free(*resTwoSum);
                    *returnSizeTwoSum = 0;
                }
            }
            else if (k == 4)
            {
                for (int counter = *prevReturnSize; counter < *returnSize; counter++)
                {
                    res[counter][0] = nums[i];
                }
                *prevReturnSize = *returnSize;
            }
        }
    }
}

int **two_sum(int *nums, int numsSize, int target, int *returnSize)
{
    int **res = NULL;
    int right = numsSize - 1;
    int left = 0;

    *returnSize = 0;
    qsort(nums, numsSize, sizeof(int), (int(*) (const void *, const void *)) comp);
    while (left < right)
    {
        int current_sum;
        current_sum = nums[left] + nums[right];
        if (current_sum < target || (left > 0 && nums[left] == nums[left - 1]))
        {
            left++;
        }
        else if (current_sum > target || (right < numsSize - 1 && nums[right] == nums[right + 1]))
        {
            right--;
        }
        else
        {
            if (res == NULL)
            {
                res = malloc(sizeof(int *));
            }
            else
            {
                res = realloc(res, sizeof(int *) * (*returnSize + 1));
            }
            res[*returnSize] = malloc(sizeof(int) * 2);
            res[*returnSize][0] = nums[left];
            res[*returnSize][1] = nums[right];
            left++;
            right--;
            (*returnSize)++;
        }
    }
    return res;
}

int comp (const int *arg1, const int *arg2)
{
    return *arg1 - *arg2;
}

