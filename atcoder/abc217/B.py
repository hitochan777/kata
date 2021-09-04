S1 = input()
S2 = input()
S3 = input()

li = ["ABC" , "ARC" , "AGC" , "AHC"]

print([x for x in li if x not in [S1, S2, S3]][0])