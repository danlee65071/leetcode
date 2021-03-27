#include <stdlib.h>

int     length_s(char   *s)
{
    int len_s;

    for (len_s = 0; s[len_s]; len_s++)
        ;
    return len_s;
}

char * convert(char * s, int numRows)
{
    char    *res;
    int     len_s;
    int     numCols;
    int     counter = 0;

    len_s = length_s(s);
    res = malloc(len_s + 1);
    if (numRows == 2)
        numCols = (len_s + 1) / numRows;
    else
        numCols = len_s / numRows;
    if (numCols == 0 || numRows == 1)
    {
        int i;
        for (i = 0; s[i]; i++)
            res[i] = s[i];
        res[i] = '\0';
        return res;
    }
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j <= numCols; j++) {
            if (i != 0 && i != numRows - 1 && j != 0)
            {
                if (j * (2 * numRows - 2) - i >= len_s)
                    break;
                res[counter++] = s[j * (2 * numRows - 2) - i];
            }
            if (i + j * (2 * numRows - 2) >= len_s)
                break;
            res[counter++] = s[i + j * (2 * numRows - 2)];
        }
    }
    res[counter] = '\0';
    return res;
}
