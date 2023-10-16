a, b, c = (int(x) for x in input().split())

if len(set([a,b,c])) == 3:
    print(0)
else:
    print(a ^ b ^ c)