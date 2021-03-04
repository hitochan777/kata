MOD = 10**9 + 7
N =int(input())
Ai = list(int(x) for x in input().split())
acc = sum(Ai)
total = 0 
for i in range(N-1):
    acc -= Ai[i]
    total = (total + Ai[i] * acc) % MOD

print(total)

