a_raw, b_raw = input().split()
a = int(a_raw)
b = int(b_raw.replace(".", ""))
print(a * b // 100)