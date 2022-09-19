N = int(input())
binN = len(bin(N)) - 2

def get_str(n, comb):
  val = 0
  for i in range(binN):
    val <<= 1
    if (n >> (binN-i-1)) & 1 == 1:
      if comb & 1 == 1:
        val += 1

      comb >>= 1
  
  return val

comb = bin(N).count("1")
ans = []
for i in range((1<<comb)):
  ans.append(get_str(N, i))

ans.sort()
for val in ans:
  print(val)