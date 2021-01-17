n, x, y = list(map(int, input().split()))
x -= 1
y -= 1
counts = [0] * (n - 1)
for i in range(n):
    for j in range(i+1, n):
        diff = min(abs(i - j), abs(i - x) + abs(j - y) + 1, abs(i - y) + abs(j - x) + 1)
        counts[diff-1] += 1

for count in counts:
    print(count)