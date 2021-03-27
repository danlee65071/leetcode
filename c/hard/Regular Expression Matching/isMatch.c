int len_p(char *p)
{
    int     len;

    for (len = 0; p[len]; len++)
        ;
    return len;
}

int isMatch(char * s, char * p)
{
    int     is_match;
    int     len_pattern;

    len_pattern = len_p(p);
    if (*p == '\0')
    {
        if (*s == '\0')
            return 1;
        else
            return 0;
    }
    if (*s != '\0' && (*p == *s || *p == '.'))
        is_match = 1;
    else
        is_match = 0;
    return ((len_pattern >= 2 && p[1] == '*') ? (isMatch(s, p+2) || (is_match && isMatch(s+1, p))) : (is_match && isMatch(s+1, p+1)));
}
