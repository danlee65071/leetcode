#include <stdio.h>
#include <stdlib.h>

int isMatch(char * s, char * p);

int main() {
    printf("%d\n", isMatch("aab", "c*a*b"));
    return 0;
}
