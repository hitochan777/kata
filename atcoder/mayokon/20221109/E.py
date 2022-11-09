from heapq import heappush, heappop
N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

max_A_bits = max(len(bin(a))-2 for a in A)
K_bits = len(bin(K))-2
max_bits = max(max_A_bits, K_bits)

ans = 0
infos = []
for i in range(max_bits-1, -1, -1):
  cnt = sum(1 for a in A if (a >> i) & 1 == 1)
  heappush(infos, (-(1<<i) * cnt, 1, i))
  heappush(infos, (-(1<<i) * (N-cnt), 0, i))

used = set()
cur = 0
ans = 0
print(infos)
while len(infos) > 0:
  val, bit, n = heappop(infos)
  val = -val
  if n in used:
    continue

  used.add(n)
  tmp = cur + (1 << n) * bit
  if tmp <= K:
    cur = tmp
    ans += val
  
print(ans)
    

    

  