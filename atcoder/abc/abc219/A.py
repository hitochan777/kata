N = int(input())
if N >= 90:
  print("expert")
elif N >= 70:
  print(90 - N)
elif N >= 40:
  print(70 - N)
else:
  print(40 - N)