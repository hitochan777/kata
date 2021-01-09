def get_count(r1, c1, r2, c2):
    r = r1 - r2
    c = c1 - c2
    if (r, c) == (0, 0):
        return 0

    if abs(r) == abs(c):
        return 1

    if abs(r) + abs(c) <= 3:
        return 1

    if  (r1 + c1 + r2 + c2) % 2 == 0:
        return 2

    if abs(r) + abs(c) <= 6:
        return 2

    if abs(r + c) <= 3 or abs(r - c) <= 3:
        return 2

    return 3

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

print(get_count(r1, c1, r2, c2))