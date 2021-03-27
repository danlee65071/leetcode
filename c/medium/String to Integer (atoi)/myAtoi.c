#include <limits.h>

int myAtoi(char * s)
{
    long res = 0;
    int i;
    int sign = 1;

    for (i = 0; s[i] == ' '; i++)
        ;
    if (s[i] == '-')
    {
        sign = -1;
        i++;
    }
    else if (s[i] == '+')
        i++;
    for (;s[i] >= '0' && s[i] <= '9'; i++)
    {
        if (res * sign >= INT_MAX)
            return INT_MAX;
        else if (res * sign <= INT_MIN)
            return INT_MIN;
        res = res * 10 + s[i] - '0';
    }
    res *= sign;
    if (res >= INT_MAX)
        return INT_MAX;
    else if (res <= INT_MIN)
        return INT_MIN;
    return res;
}
