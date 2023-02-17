X, Y = (int(x) for x in input().split())
MOD = 10**9 + 7

def ncr(n, r, p):
    num = den = 1 
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, 
            p - 2, p)) % p

a = 2 * X - Y
b = 2 * Y - X
# print(a,b)
if a < 0 or b < 0 or a % 3 != 0 or b % 3 != 0:
    print(0)
    exit()

a //= 3
b //= 3
ans = ncr(a+b, a, MOD)
print(ans)