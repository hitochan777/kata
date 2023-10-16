def get_depth(node):
  depth = 0
  while node > 0:
    node >>= 1
    depth += 1
    
  return depth

def get_num_desc(node, d, N):
  val = min((node+1)*(1<<d), N) - min(node*(1<<d), N) + 1
  # print("val", val)
  return val

def solve(N, X, K):
  node = X
  dist_to_lca = 0
  cnt = 0
  while node > 0:
    # print(K, dist_to_lca)
    if K - dist_to_lca < 0:
      break

    diff = get_num_desc(node, K-dist_to_lca, N)
    if dist_to_lca > 0 and K-dist_to_lca-1>0:
      is_left = (node * 2 + 1) * (1<<(dist_to_lca-1)) < X
      # print(dist_to_lca-1, K-dist_to_lca-1)
      diff -= get_num_desc(node*2+(0 if is_left else 1),K-dist_to_lca-1,N)

    print(get_num_desc(node, K-dist_to_lca, N), "diff:", diff)

    cnt += diff
    dist_to_lca += 1
    node >>= 1

  return cnt

T = int(input())
for _ in range(T):
  N, X, K = (int(x) for x in input().split())
  ans = solve(N, X, K) 
  print(ans)
# print(get_num_desc(1, 3, 10))