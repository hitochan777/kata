from collections import Counter
S = input()[::-1]
MOD = 2019

X = [0]
for i, s in enumerate(S):
    X.append((X[-1] + int(s) * pow(10, i, MOD)) % MOD)

print(X)

C = Counter(X)
ans = 0
for v in C.values():
    ans += v * (v - 1) // 2
print(ans)
