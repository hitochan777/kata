N, X, M = (int(x) for x in input().split())


def f(a):
    return a**2 % M

a = X
s = {X: 0}
total = X
size, first = None, 0
for i in range(1, M+1):
    a = f(a)
    if a in s:
        size = i - s[a]
        first = s[a]
        break

    total += a
    s[a] = i

rem = N - len(s)
a = X
former = 0
for i in range(first):
    former += a
    a = f(a)

repeating_total = total - former

total += repeating_total * (rem // size)

a = X
for i in range(first + rem % size):
    if i >= first:
        total += a

    a = f(a)

print(total)
