N = int(input())-1
print(bin(N)[2:].zfill(10).replace("0", "4").replace("1", "7"))