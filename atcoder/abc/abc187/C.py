from collections import defaultdict

def read_int():
    return int(input())

def solve() -> str:
    n = read_int()
    map = defaultdict(int)
    for _ in range(n):
        s = input()
        if s.startswith("!"):
            map[s[1:]] |= 1 << 1
            if map[s[1:]] == 3:
                return s[1:]
        else:
            map[s] |= 1 << 0
            if map[s] == 3:
                return s

    return "satisfiable"

print(solve())