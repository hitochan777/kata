import sys
I=sys.stdin.readline

def solve():
    n = int(I())
    es = list(map(int, I().split()))
    es = sorted(es)
    i, start = 0, 0
    cnt = 0
    while start < n:
        i = start + es[i]
        while i <= n and i - start < es[i-1]:
            i += 1

        if i <= n:
            cnt += 1
        else:
            break 

        start = i

    return cnt

if __name__ == "__main__":
    n = int(I())
    for _ in range(n):
        print(solve())
