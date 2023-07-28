def transpose_list_of_strings(strings_list):
    list_of_lists = [list(string) for string in strings_list]
    transposed_lists = list(zip(*list_of_lists))
    transposed_strings = [''.join(characters) for characters in transposed_lists]
    return transposed_strings

H, W = (int(x) for x in input().split())
S = []
for _ in range(H):
  S.append(input())
  
S = transpose_list_of_strings(S)
S.sort()

T = []
for _ in range(H):
  T.append(input())

T = transpose_list_of_strings(T)
T.sort()
# print(S)
# print(T)
if all(s == t for s, t in zip(S, T)):
   print("Yes")
else:
   print("No")