N = int(input())
total = 0
n = 1
while total < N:
  total += n
  n += 1

ex = total - N
ans = [str(i) for i in range(1, n) if i != ex]
print(" ".join(ans))