t = int(input())
def get_mem():
  N = 10**3
  min_ops = [10**18] * (N+1)
  min_ops[1] = 0
  for i in range(1, N+1):
    for j in range(1, i+1):
      if i + i // j > N:
        continue

      min_ops[i + i // j] = min(min_ops[i]+1, min_ops[i + i // j])

  return min_ops

dp = get_mem()
for _ in range(t):
  n, k = (int(x) for x in input().split())
  B = list(int(x) for x in input().split())
  C = list(int(x) for x in input().split())

  w = [dp[b] for b in B]
  def knapsack(W, wt, val, n):
      K = [[0 for x in range(W + 1)] for x in range(2)]
      for i in range(n + 1):
          for w in range(W + 1):
              if i == 0:
                  K[i%2][w] = 0
              elif wt[i-1] <= w:
                K[i % 2][w] = max(val[i - 1] + K[(i - 1) % 2][w - wt[i - 1]], K[(i - 1) % 2][w])
              else:
                K[i%2][w] = K[(i-1)%2][w]
      return K[n%2][W]

  print(knapsack(min(12*1001, k), w, C, n))