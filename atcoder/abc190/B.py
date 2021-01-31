N, S, D = list(map(int, input().split()))
cnt = 0
for _ in range(N):
    X, Y = list(map(int, input().split()))
    if X < S and Y > D:
        cnt += 1

print("Yes" if cnt > 0 else "No")