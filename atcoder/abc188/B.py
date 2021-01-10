n = int(input())
a_list =  list(map(int, input().split()))
b_list =  list(map(int, input().split()))

total = 0
for i in range(n):
    total += a_list[i] * b_list[i]

print("Yes" if total == 0 else "No")
