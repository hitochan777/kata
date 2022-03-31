N, M = (int(x) for x in input().split())
print((pow(10, N, M**2) // M) % M)