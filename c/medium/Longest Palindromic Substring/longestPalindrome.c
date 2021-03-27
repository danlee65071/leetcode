#include <stdlib.h>

int around_center(char *s, int ind_left, int ind_right)
{
    int L = ind_left;
    int R = ind_right;
    
    while((L >= 0 && s[R]) && (s[L] == s[R]))
    {
        L--;
        R++;
    }
    return R - L - 1;
}

char* longestPalindrome(char* s) {
    int len_sub = 0;
    int start = 0;
    int end = 0;
    int len1 = 0;
    int len2 = 0;
    char *sub = NULL;
    int j = 0;

    for (int i = 0; s[i]; i++)
    {
        len1 = around_center(s, i, i);
        len2 = around_center(s, i, i + 1);
        if (len1 >= len2)
            len_sub = len1;
        else
            len_sub = len2;
        if (len_sub > end - start)
        {
            start = i - (len_sub - 1) / 2;
            end = i + len_sub / 2;
        }
    }
    if (sub != NULL)
        free(sub);
    sub = malloc(end - start + 2);
    for (int i = start; i <= end; i++, j++)
        sub[j] = s[i];
    sub[j] = '\0';
    return sub;
}
