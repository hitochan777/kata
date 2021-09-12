N = int(input())
denoms = [100, 20, 10, 5, 1]

bills = 0
for denom in denoms:
  new_bills = N // denom
  N -= new_bills * denom
  bills += new_bills

print(bills)