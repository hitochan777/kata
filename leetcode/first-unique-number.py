from typing import List

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, value):
        new_node = DoublyLinkedListNode(None, None, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return new_node

    def remove(self, node):
        if node is None:
            return

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if self.head is node:
            self.head = node.next

        if self.tail is node:
            self.tail = node.prev

        return

    def __str__(self):
        ptr = self.head
        li = []
        while ptr is not None:
            val = ptr.value
            li.append(f"{val}")
            ptr = ptr.next

        return ", ".join(li)


class DoublyLinkedListNode:
    def __init__(self, prev, _next, value):
        self.prev = prev
        self.next = _next
        self.value = value


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.exists = {}
        self.dll = DoublyLinkedList()
        for num in nums:
            self.add(num)


    def showFirstUnique(self) -> int:
        if self.dll.head is None:
            return -1

        return self.dll.head.value


    def add(self, value: int) -> None:
        if value in self.exists:
            self.dll.remove(self.exists[value])
            return

        new_node = self.dll.add(value)
        self.exists[value] = new_node


if __name__ == "__main__":
    firstUnique = FirstUnique([2,3,5]);
    assert firstUnique.showFirstUnique() == 2
    firstUnique.add(5)
    assert firstUnique.showFirstUnique() == 2
    firstUnique.add(2)
    assert firstUnique.showFirstUnique() == 3
    firstUnique.add(3)
    assert firstUnique.showFirstUnique() == -1


    firstUnique = FirstUnique([809])
    assert firstUnique.showFirstUnique() == 809
    firstUnique.add(809)
    assert firstUnique.showFirstUnique() == -1

    firstUnique = FirstUnique([7,7,7,7,7,7])
    assert firstUnique.showFirstUnique() == -1
    firstUnique.add(7)
    firstUnique.add(3)
    firstUnique.add(3)
    firstUnique.add(7)
    firstUnique.add(17)
    assert firstUnique.showFirstUnique() == 17

    firstUnique = FirstUnique([1, 1, 7, 7, 6])
    firstUnique.add(6)
    firstUnique.add(2)
    assert firstUnique.showFirstUnique() == 2

    firstUnique = FirstUnique([])
    assert firstUnique.showFirstUnique() == -1

    firstUnique = FirstUnique([1, 2, 3])
    firstUnique.add(1)
    firstUnique.add(3)
    assert firstUnique.showFirstUnique() == 2
