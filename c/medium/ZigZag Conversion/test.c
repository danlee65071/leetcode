#include <stdio.h>
#include <stdlib.h>

char * convert(char * s, int numRows);

int main() {
    char    s[] = "PAYPALISHIRING";
    char    *res;

    res = convert(s, 4);
    printf("%s\n", res);
    free(res);
    res = convert(s, 3);
    printf("%s\n", res);
    free(res);
    res = convert("A", 2);
    printf("%s\n", res);
    free(res);
    res = convert("AB", 1);
    printf("%s\n", res);
    free(res);
    res = convert("ABC", 1);
    printf("%s\n", res);
    free(res);
    res = convert("ABCD", 2);
    printf("%s\n", res);
    free(res);
    res = convert(s, 2);
    printf("%s\n", res);
    free(res);
    res = convert("ABC", 2);
    printf("%s\n", res);
    free(res);
    res = convert("ABCD", 3);
    printf("%s\n", res);
    free(res);
    res = convert("ABC", 3);
    printf("%s\n", res);
    free(res);
    return 0;
}
