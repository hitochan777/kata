a, b = input().split()
a_sum = sum(map(int, a))
b_sum = sum(map(int, b))
print(max(a_sum, b_sum))
