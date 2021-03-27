int lengthOfLongestSubstring(char * s)
{
    int i;
    int j;
    int len;
    int max_len;
    int a;

    max_len = 1;
    a = 0;
    i = 1;
    if (*s == '\0')
        return (0);
    while (s[i]) {
        j = a;
        len = 1;
        while (j < i) {
            if (s[i] == s[j]) {
                a = j + 1;
                break ;
            }
            len++;
            if (len > max_len)
                max_len = len;
            j++;
        }
        i++;
    }
    return (max_len);
}
