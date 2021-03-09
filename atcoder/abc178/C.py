N = int(input())

mod = 10 ** 9 + 7

def powmod(x, n):
    val = 1
    for _ in range(n):
        val *= x
        val %= mod

    return val

ans = powmod(10, N) - 2 * powmod(9, N) + powmod(8, N)
print(ans % mod)