N = int(input())

ans = sum(N / k for k in range(N - 1, 0, -1))
print(ans)