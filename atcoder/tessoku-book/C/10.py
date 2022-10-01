W = int(input())
MOD = 1000000007

# ans = 12 * 7^(W-1)
print((12 * pow(7, W-1, MOD)) % MOD)