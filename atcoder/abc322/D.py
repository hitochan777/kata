def rotate90(grid):
  new_grid = []
  for i in range(0, len(grid)):
      row = [] # row of 3x4 matrix
      for j in range(0, len(grid[0])):
          row.append(grid[j][i])
      row.reverse()  # So that we gat the desired order
      new_grid.append(row)
  
  return new_grid

def enum_placement(grid):
    for _ in range(4):
      for i in range(4):
        for j in range(4):
          result_matrix = [["." for _ in range(8)] for _ in range(8)]
          for row in range(4):
            for col in range(4):
              # print(i,j,row, col, grid)
              result_matrix[i+row][j+col] = grid[row][col]

          yield result_matrix 

      grid = rotate90(grid)

def has_4x4_a(matrix):
    # Define the dimensions of the input matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Iterate through the input matrix
    for i in range(num_rows - 3):  # Loop through rows
        for j in range(num_cols - 3):  # Loop through columns
            # Check if the 4x4 submatrix starting at (i, j) is all "a"
            if all(matrix[row][col] == '#' for row in range(i, i + 4) for col in range(j, j + 4)):
                return True

    # If no 4x4 "a" submatrix is found, return False
    return False

def overlap(g1, g2):
  li = [["." for _ in range(8)] for _ in range(8)]
  for i in range(8):
    for j in range(8):
      li[i][j] = g1[i][j]

  for i in range(8):
    for j in range(8):
      if li[i][j] != "." and g2[i][j] != ".":
        return (False, None)

      li[i][j] = g2[i][j]
    
  return (True, li)

P = [[] for _ in range(3)]
for i in range(3):
  for j in range(4):
    P[i].append(list(input()))

g1 = enum_placement(P[0])
g2 = enum_placement(P[1])
g3 = enum_placement(P[2])

for p1 in g1:
  grid = p1
  for p2 in g2:
    ok, grid2 = overlap(grid, p2)
    if not ok:
       continue

    for p3 in g3:
      ok, grid3 = overlap(grid2, p3)
      if not ok:
        continue


      print("yeaw")
      if has_4x4_a(grid3):
         print("Yes")
         exit()


print("No")