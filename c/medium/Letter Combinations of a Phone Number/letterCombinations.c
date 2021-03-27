#include <stdlib.h>

int len_s(char *s)
{
    int len_word = 0;

    for (len_word = 0; s[len_word]; len_word++)
        len_word++;
    return len_word;
}

char **itertools_product_str(char **iter_arr, int len_iter_arr)
{
    char **res;

    
}
