#include <stdlib.h>

int comp(const int *arg1, const int *arg2)
{
    return *arg1 - *arg2;
}

int threeSumClosest(int* nums, int numsSize, int target)
{
    int sum;
    int diff;
    int j, k;
    int tmp;

    qsort(nums, numsSize, sizeof (int), (int(*) (const void *, const void *)) comp);
    sum = nums[0] + nums[1] + nums[2];
    diff = abs(target - (nums[0] + nums[1] + nums[2]));
    for (int i = 0; i < numsSize - 2; i++)
    {
        j = i + 1;
        k = numsSize - 1;
        while(j < k)
        {
            tmp = nums[i] + nums[j] + nums[k];
            if (abs(target - tmp) < diff)
            {
                sum = tmp;
                diff = abs(target - tmp);
            }
            if (tmp < target)
                j++;
            else if (tmp > target)
                k--;
            else if (tmp == target)
                break;
        }
    }
    return sum;
}
