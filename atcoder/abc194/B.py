N = list(int(x) for x in input().split())[0]

min_val = 10**6
times = []
for _ in range(N):
    A, B = list(int(x) for x in input().split())
    times.append((A, B))

for i in range(N):
    for j in range(N):
        A = times[i][0]
        B = times[j][1]
        if i == j:
            val = A + B
        else:
            val = max(A, B)

        min_val = min(min_val, val)

print(min_val)
