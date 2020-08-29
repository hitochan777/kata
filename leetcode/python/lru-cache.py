class DoublyLinkedListNode:
    def __init__(self, prev, _next, key, value):
        self.prev = prev
        self.next = _next
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.dll = None
        self.mru_node = None
        self.cap = capacity
        self.map = {}

    def touch(self, node: DoublyLinkedListNode) -> None:
        if node is self.mru_node:
            return

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev
            if self.dll is node:
                self.dll = node.next

        node.prev = self.mru_node
        node.next = None
        self.mru_node.next = node
        self.mru_node = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.touch(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            self.touch(self.map[key])
            return

        if self.cap <= len(self.map):
            if self.map[self.dll.key] is self.mru_node:
                self.mru_node = None

            del self.map[self.dll.key]
            if self.dll.next is not None:
                self.dll.next.prev = None

            self.dll = self.dll.next

        new_node = DoublyLinkedListNode(None, None, key, value)
        if len(self.map) == 0:
            self.dll = new_node
        else:
            self.mru_node.next = new_node
            new_node.prev = self.mru_node

        self.map[key] = new_node
        self.mru_node = new_node

    def print_linked_list(self):
        node = self.dll
        while node is not None:
            print(f"{node.key}", end=",")
            node = node.next

        print()

    def print_map(self):
        for key, node in self.map.items():
            print(f"{key}: {node.value}")


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4 

    cache = LRUCache(1)
    cache.put(2, 1)
    assert cache.get(1) == -1

    cache = LRUCache(1)
    cache.put(2, 1)
    assert cache.get(2) == 1
    cache.put(3, 2)
    assert cache.get(2) == -1
    assert cache.get(3) == 2

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    assert cache.get(2) == 2
    cache.put(1, 1)
    cache.put(4, 1)
    assert cache.get(2) == -1

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(3, 2)
    assert cache.get(3) == 2
    assert cache.get(2) == 1
    cache.put(4, 3)
    assert cache.get(2) == 1
    assert cache.get(3) == -1
    assert cache.get(4) == 3
