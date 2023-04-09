def gcd_cnt(a, b):
    cnt = 0
    while b:
        cnt += a//b
        a, b = b, a%b
    return cnt

A, B = (int(x) for x in input().split())
ans = gcd_cnt(A, B) - 1
print(ans)