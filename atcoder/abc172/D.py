# 1     2   3  4 
# f(1) f(2)
# 1     1    1 1 1 1
#       2    4   
#       1    1   1

total = 0
n = int(input())
for i in range(1, n+1):
    m = n // i
    total += i * m * (m + 1) // 2

print(total)
    