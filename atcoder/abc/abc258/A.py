K = int(input())

h = str(21 + K // 60).zfill(2)
m = str(K % 60).zfill(2)
print(f"{h}:{m}")