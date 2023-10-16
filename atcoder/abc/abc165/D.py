A, B, N = ( int(w) for w in  input().split() )
max_val = 0
x = min(B-1, N)
first = A * x // B
second = A * (x // B)

print(first - second)
