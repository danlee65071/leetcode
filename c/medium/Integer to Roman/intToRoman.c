#include <stdlib.h>
#include <string.h>

char *digit_to_roman(int digit, int rank)
{
    char *roman_digit;
    char rank_symbols[3];
    int  i;

    roman_digit = malloc(1);
    if (rank == 0)
    {
        rank_symbols[0] = 'I';
        rank_symbols[1] = 'V';
        rank_symbols[2] = 'X';
    }
    else if (rank == 1)
    {
        rank_symbols[0] = 'X';
        rank_symbols[1] = 'L';
        rank_symbols[2] = 'C';
    }
    else if (rank == 2)
    {
        rank_symbols[0] = 'C';
        rank_symbols[1] = 'D';
        rank_symbols[2] = 'M';
    }
    else if (rank == 3)
    {
        rank_symbols[0] = 'M';
    }
    if (digit < 5 && digit != 4)
    {
        for (i = 0; i < digit; i++)
        {
            roman_digit = realloc(roman_digit, i+1);
            roman_digit[i] = rank_symbols[0];
        }
        roman_digit = realloc(roman_digit, i+1);
        roman_digit[i] = '\0';
    }
    else if (digit == 4)
    {
        roman_digit = realloc(roman_digit, 3);
        roman_digit[0] = rank_symbols[0];
        roman_digit[1] = rank_symbols[1];
        roman_digit[2] = '\0';
    }
    else if (digit == 5)
    {
        roman_digit = realloc(roman_digit, 2);
        roman_digit[0] = rank_symbols[1];
        roman_digit[1] = '\0';
    }
    else if (digit > 5 && digit < 9)
    {
        roman_digit[0] = rank_symbols[1];
        for (i = 1; i < digit-4; i++)
        {
            roman_digit = realloc(roman_digit, i+2);
            roman_digit[i] = rank_symbols[0];
        }
        roman_digit = realloc(roman_digit, i+1);
        roman_digit[i] = '\0';
    }
    else if (digit == 9)
    {
        roman_digit = realloc(roman_digit, 3);
        roman_digit[0] = rank_symbols[0];
        roman_digit[1] = rank_symbols[2];
        roman_digit[2] = '\0';
    }
    return roman_digit;
}

char *front_insert(char *s, char *ins_s)
{
    char *tmp;
    int i;
    int n;
    int k;

    tmp = malloc(strlen(s) + 1);
    for (i = 0; s[i]; i++)
        tmp[i] = s[i];
    n = i;
    for (i = 0; ins_s[i]; i++)
        s[i] = ins_s[i];
    k = i;
    for (int j = 0; i < n + k; i++, j++)
        s[i] = tmp[j];
    return s;
}

char *intToRoman(int num)
{
    char *roman_num;
    char *digit_roman;
    int i = 0;

    roman_num = malloc(1);
    *roman_num = '\0';
    while(num != 0)
    {
        digit_roman = digit_to_roman(num % 10, i);
        if (*roman_num == '\0')
            roman_num = realloc(roman_num, strlen(digit_roman) + 1);
        else
            roman_num = realloc(roman_num, strlen(digit_roman) + strlen(roman_num) + 1);
        roman_num[strlen(digit_roman) + strlen(roman_num)] = '\0';
        front_insert(roman_num, digit_roman);
        free(digit_roman);
        num /= 10;
        i++;
    }
    return roman_num;
}
