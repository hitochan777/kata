def get_depth(node):
  depth = 0
  while node > 0:
    node >>= 1
    depth += 1
    
  return depth

def get_num_desc(node, d, N):
  return min((node+1)*(1<<d), N) - node*(1<<d)

def solve(N, X, K):
  node = X
  dist_to_lca = 0
  cnt = 0
  while node > 0:
    if K - dist_to_lca - 1 < 0:
      break

    cnt += get_num_desc(node, K-dist_to_lca, N) - get_num_desc(node*2,K-dist_to_lca-1,N)
    dist_to_lca += 1
    node >>= 1

  return cnt

T = int(input())
for _ in range(T):
  N, X, K = (int(x) for x in input().split())
  ans = solve(N, X, K) 
  print(ans)
# print(get_num_desc(2, 1, 8))
