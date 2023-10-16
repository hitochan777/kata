from collections import defaultdict
N, K = list(map(int, input().split()))
al = list(map(int, input().split()))

indices = defaultdict(int)
cur = 0
index = 0
loop_size = None
connected_items = []
while True:
    if cur in indices:
        loop_size = len(connected_items) - indices[cur]
        break

    indices[cur] = index
    connected_items.append(cur)
    cur = al[cur] - 1
    index += 1
    
non_loop_size = len(connected_items) - loop_size
# print(non_loop_size)
final_index =  (K - non_loop_size) % loop_size + non_loop_size if K >= len(connected_items) else K
print(connected_items[final_index]+1)