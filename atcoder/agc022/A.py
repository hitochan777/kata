from collections import Counter
from typing import Optional
from string import ascii_lowercase

S = input()

def get_diverse_word(s: str) -> Optional[str]:
    if len(s) == 26:
        return None

    for c in ascii_lowercase:
        if c in s:
            continue

        return s + c 

    return None

maybe_word = get_diverse_word(S)
print(-1 if maybe_word is None else maybe_word)
