class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or sorted(A) != sorted(B) or (A == B and len(set(A)) == len(A)):
            return False

        diff_cnt = sum(1 for a, b in zip(A, B) if a != b)
        return diff_cnt in [0, 2]
