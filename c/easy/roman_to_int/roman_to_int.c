typedef struct	s_roman
{
	char		c;
	int		n;
	struct	s_roman	*next;
}		t_roman;

int	give_int(char c)
{
	t_roman	*begin;
	t_roman	I;
	t_roman	V;
	t_roman	X;
	t_roman	L;
	t_roman	C;
	t_roman	D;
	t_roman	M;
	t_roman	*tmp;

	begin = &I;
	I.c = 'I';
	I.n = 1;
	I.next = &V;
	V.c = 'V';
	V.n = 5;
	V.next = &X;
	X.c = 'X';
	X.n = 10;
	X.next = &L;
	L.c = 'L';
	L.n = 50;
	L.next = &C;
	C.c = 'C';
	C.n = 100;
	C.next = &D;
	D.c = 'D';
	D.n = 500;
	D.next = &M;
	M.c = 'M';
	M.n = 1000;
	M.next = 0;
	tmp = begin;
	while (tmp)
	{
		if (tmp->c == c)
			return (tmp->n);
		tmp = tmp->next;
	}
	return (0);
}

int romanToInt(char * s)
{
	int	len;
	int	res;
	int	previous;

	previous = 0;
	len = 0;
	res = 0;
	while (s[len++])
		;
	len--;
	previous = give_int(s[len]);
	res = previous;
	len--;
	while (len >= 0)
	{
		if (previous > give_int(s[len]))
			res -= give_int(s[len]);
		else
			res += give_int(s[len]);
		previous = give_int(s[len]);
		len--;
	}
	return (res);
}
