n = int(input())
a = list(map(int, input().split()))
a.sort()
a = a[::-1]
total = a[0]
for i in range(n-2):
  total += a[1 + i//2]

print(total)
