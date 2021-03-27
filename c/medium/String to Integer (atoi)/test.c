#include <stdio.h>
#include <stdlib.h>

int myAtoi(char * s);

int main() {
    char    s[] = "   -42";

    printf("%d\n", myAtoi(s));
    printf("%d\n", myAtoi("4193 with words"));
    printf("%d\n", myAtoi("words and 987"));
    printf("%d\n", myAtoi("-91283472332"));
    printf("%d\n", myAtoi("+1"));
    printf("%d\n", myAtoi("20000000000000000000"));
    printf("%d\n", myAtoi("21474836460"));
    return 0;
}
