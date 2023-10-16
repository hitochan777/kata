def shift_clockwise(grid):
    n = len(grid)
    shifted_grid = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_i, new_j = i, j
            if i == 0:
              new_j = min(j+1, n-1)
              if j == n - 1:
                 new_i = i + 1
            elif i == n - 1:
              new_j = max(j-1, 0)
              if j == 0:
                 new_i = i-1
            elif j == 0:
              new_i = max(i-1, 0)
            elif j == n - 1:
              new_i = min(i+1, n-1)

            # print(i, j, new_i, new_j)
            shifted_grid[new_i][new_j] = grid[i][j]
    
    return shifted_grid

N = int(input())
grid = []
for _ in range(N):
  row = input() 
  grid.append(row)

new_grid = shift_clockwise(grid)
for row in new_grid:
    print("".join(map(lambda s: str(s), row)))