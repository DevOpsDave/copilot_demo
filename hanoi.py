#!/usr/bin/env python


def hanio(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanio(n-1, a, c, b)
        print(a, '-->', c)
        hanio(n-1, b, a, c)
        
hanio(3, 'A', 'B', 'C')


