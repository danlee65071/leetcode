#include <stdlib.h>
#include <string.h>

void itertools_product_str(char **arr, int len_arr, char **res, char *tmp)
{
    if (strlen(tmp) == len_arr)
    {
        *(tmp + len_arr) = '\0';
        while (**res != '\0')
        {
            res++;
        }
        *res = strcat(*res, tmp);
        return;
    }
    for (int i = 0; *(*arr + i); i++)
    {
        int len_res = strlen(tmp);
        *(tmp + len_res) = *(*arr + i);
        itertools_product_str(arr + 1, len_arr, res, tmp);
        tmp[len_res] = '\0';
    }
}

char ** letterCombinations(char * digits, int* returnSize)
{
    char *digits_map[] = {"abc", "def", "ghi", "jkl",
                            "mno", "pqrs", "tuv", "wxyz"};
    char **iter_arr;
    int len_iter_arr;
    char **res;
    char *tmp;

    if (digits == NULL || strlen(digits) == 0)
    {
        *returnSize = 0;
        return NULL;
    }
    *returnSize = 1;
    len_iter_arr = strlen(digits);
    iter_arr = malloc(sizeof(char *) * (len_iter_arr + 1));
    for (int i = 0; digits[i]; i++)
    {
        iter_arr[i] = malloc(sizeof(char) * (strlen(digits_map[(int)(digits[i] - '0') - 2]) + 1));
        *returnSize *= strlen(digits_map[(int)(digits[i] - '0') - 2]);
    }
    iter_arr[len_iter_arr] = NULL;
    for (int i = 0; i < len_iter_arr; i++)
    {
        for (int j = 0; j < strlen(digits_map[(int)(digits[i] - '0') - 2]); j++)
        {
            iter_arr[i][j] = digits_map[(int)(digits[i] - '0') - 2][j];
        }
        iter_arr[i][strlen(digits_map[(int)(digits[i] - '0') - 2])] = '\0';
    }
    res = malloc(sizeof(char *) * *returnSize);
    tmp = malloc(sizeof(char) * (len_iter_arr + 1));
    for (int i = 0; i < *returnSize; i++)
    {
        res[i] = malloc(sizeof(char) * (len_iter_arr + 1));
        for (int j = 0; j < len_iter_arr + 1; j++)
        {
            res[i][j] = '\0';
            tmp[j] = '\0';
        }
    }
    itertools_product_str(iter_arr, len_iter_arr, res, tmp);
    for (int i = 0; digits[i]; i++)
    {
        free(iter_arr[i]);
    }
    free(iter_arr);
    free(tmp);
    return res;
}
