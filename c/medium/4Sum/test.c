#include <stdio.h>
#include <stdlib.h>

int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes);

int main()
{
    //test1
    int nums1[] = {1, 0, -1, 0, -2, 2};
    int target1 = 0;
    int returnSize1 = 0;
    int *returnColumnSizes1 = NULL;
    int **res1;

    res1 = fourSum(nums1, 6, target1, &returnSize1, &returnColumnSizes1);
    printf("test1\nres1:\n");
    for (int i = 0; i < returnSize1; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", res1[i][j]);
        }
        printf("\n");
    }
    printf("returnSize1 = %d\n", returnSize1);
    printf("returnColumnSizes1:\n");
    for (int i = 0; i < returnSize1; i++)
    {
        printf("%d ", returnColumnSizes1[i]);
    }
    printf("\n");
    
    //test2
    int nums2[0];
    int target2 = 0;
    int returnSize2 = 0;
    int *returnColumnSizes2 = NULL;
    int **res2;

    res2 = fourSum(nums2, 0, target2, &returnSize2, &returnColumnSizes2);
    printf("\ntest2\nres2:\n");
    for (int i = 0; i < returnSize2; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", res2[i][j]);
        }
        printf("\n");
    }
    printf("returnSize2 = %d\n", returnSize2);
    printf("returnColumnSizes2:\n");
    for (int i = 0; i < returnSize2; i++)
    {
        printf("%d ", returnColumnSizes2[i]);
    }
    printf("\n");
    
    //test3
    int nums3[] = {-2, -1, -1, 1, 1, 2, 2};
    int target3 = 0;
    int returnSize3 = 0;
    int *returnColumnSizes3 = NULL;
    int **res3;

    res3 = fourSum(nums3, 7, target3, &returnSize3, &returnColumnSizes3);
    printf("\ntest3\nres3:\n");
    for (int i = 0; i < returnSize3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", res3[i][j]);
        }
        printf("\n");
    }
    printf("returnSize3 = %d\n", returnSize3);
    printf("returnColumnSizes3:\n");
    for (int i = 0; i < returnSize3; i++)
    {
        printf("%d ", returnColumnSizes3[i]);
    }
    printf("\n");
    
    //test4
    int nums4[] = {-3, -1, 0, 2, 4, 5};
    int target4 = 2;
    int returnSize4 = 0;
    int *returnColumnSizes4 = NULL;
    int **res4;

    res4 = fourSum(nums4, 6, target4, &returnSize4, &returnColumnSizes4);
    printf("\ntest4\nres4:\n");
    for (int i = 0; i < returnSize4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", res4[i][j]);
        }
        printf("\n");
    }
    printf("returnSize4 = %d\n", returnSize4);
    printf("returnColumnSizes4:\n");
    for (int i = 0; i < returnSize4; i++)
    {
        printf("%d ", returnColumnSizes4[i]);
    }
    printf("\n");
    
    //test5
    int nums5[] = {-3, -2, -1, 0, 0, 1, 2, 3};
    int target5 = 0;
    int returnSize5 = 0;
    int *returnColumnSizes5 = NULL;
    int **res5;

    res5 = fourSum(nums5, 8, target5, &returnSize5, &returnColumnSizes5);
    printf("\ntest5\nres5:\n");
    for (int i = 0; i < returnSize5; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", res5[i][j]);
        }
        printf("\n");
    }
    printf("returnSize5 = %d\n", returnSize5);
    printf("returnColumnSizes5:\n");
    for (int i = 0; i < returnSize5; i++)
    {
        printf("%d ", returnColumnSizes5[i]);
    }
    printf("\n");
    
    //test6
    int nums6[] = {-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5};
    int target6 = 0;
    int returnSize6 = 0;
    int *returnColumnSizes6 = NULL;
    int **res6;

    res6 = fourSum(nums6, 12, target6, &returnSize6, &returnColumnSizes6);
    printf("\ntest6\nres6:\n");
    for (int i = 0; i < returnSize6; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", res6[i][j]);
        }
        printf("\n");
    }
    printf("returnSize6 = %d\n", returnSize6);
    printf("returnColumnSizes6:\n");
    for (int i = 0; i < returnSize6; i++)
    {
        printf("%d ", returnColumnSizes6[i]);
    }
    printf("\n");
    
    //test7
    int nums7[] = {-5,5,4,-3,0,0,4,-2};
    int target7 = 4;
    int returnSize7 = 0;
    int *returnColumnSizes7 = NULL;
    int **res7;

    res7 = fourSum(nums7, 8, target7, &returnSize7, &returnColumnSizes7);
    printf("\ntest7\nres7:\n");
    for (int i = 0; i < returnSize7; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", res7[i][j]);
        }
        printf("\n");
    }
    printf("returnSize7 = %d\n", returnSize7);
    printf("returnColumnSizes7:\n");
    for (int i = 0; i < returnSize7; i++)
    {
        printf("%d ", returnColumnSizes7[i]);
    }
    printf("\n");
    
    //test8
    int nums8[] = {-3,0,7,-2,-6,-5,1,5,-1,-8,-9,-8,7,1,1,3,1,10};
    int target8 = 0;
    int returnSize8 = 0;
    int *returnColumnSizes8 = NULL;
    int **res8;

    res8 = fourSum(nums8, 18, target8, &returnSize8, &returnColumnSizes8);
    printf("\ntest8\nres8:\n");
    for (int i = 0; i < returnSize8; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d ", res8[i][j]);
        }
        printf("\n");
    }
    printf("returnSize8 = %d\n", returnSize7);
    printf("returnColumnSizes8:\n");
    for (int i = 0; i < returnSize8; i++)
    {
        printf("%d ", returnColumnSizes8[i]);
    }
    printf("\n");
    
    return 0;
}

