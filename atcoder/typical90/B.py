from typing import List

def dfs(s: str, level: int, n: int) -> List[str]:
  if len(s) >= n:
    return [s] if level == 0 else []
   
  if level < 0:
    return []

  res = []
  res += dfs(s + "(", level + 1, n)
  res += dfs(s + ")", level - 1, n)
  return res

N = int(input())
print("\n".join(dfs("", 0, N)))

