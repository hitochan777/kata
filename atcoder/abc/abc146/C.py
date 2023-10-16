A, B, X = (int(x) for x in input().split())

def cost(n):
    return A * n + B * len(str(n))

def solve():
    l, h = 1, 10**9
    while l < h:
        m = (l + h) >> 1
        c = cost(m)
        if c == X:
            return m
        elif c < X:
            l = m + 1
        else:
            h = m - 1

    if l == h:
        if cost(l) <= X:
            return l

        return l - 1

    return 0

print(solve())
