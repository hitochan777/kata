from typing import List
def show_real(chars: List[str], flipped: bool) -> str:
    n = len(chars) >> 1
    new_chars = chars[:]
    if flipped:
        new_chars = chars[n:] + chars[:n]

    print("".join(new_chars))


N = int(input())
S = list(input())
Q = int(input())
flipped = False
for _ in range(Q):
    T, A, B = (int(x) for x in input().split())
    if T == 1:
        A -= 1
        B -= 1
        if flipped:
            A = (A + N) % (2 * N)
            B = (B + N) % (2 * N)
        
        S[A], S[B] = S[B], S[A]
    else:
        flipped = not flipped 

show_real("".join(S), flipped)