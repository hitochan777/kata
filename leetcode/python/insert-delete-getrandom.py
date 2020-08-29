import random

class RandomizedSet:

    def __init__(self):
        self.val2idx = {}
        self.idx2val = {}
        

    def insert(self, val: int) -> bool:
        if val in self.val2idx:
            return False
        
        size = len(self.val2idx)
        self.val2idx[val] = size
        self.idx2val[size] = val
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.val2idx:
            return False
        
        idx = self.val2idx[val]
        del self.val2idx[val]
        del self.idx2val[idx]
        size = len(self.val2idx)
        if size > 0 and idx < size:
            val = self.idx2val[idx] = self.idx2val[size]
            self.val2idx[val] = idx
            del self.idx2val[size]
            
        return True

    def getRandom(self) -> int:
        size = len(self.val2idx)
        if size == 0:
            return -1
        
        idx = random.randint(0, size - 1)
        return self.idx2val[idx]


if __name__ == "__main__":
    rs = RandomizedSet()
    rs.insert(3)
    rs.insert(3)
    print(rs.getRandom())
    print(rs.getRandom())
    rs.insert(1)
    rs.remove(3)
    print(rs.getRandom())
    print(rs.getRandom())
    rs.insert(0)

    print(rs.val2idx)
    print(rs.idx2val)
    rs.remove(0)
