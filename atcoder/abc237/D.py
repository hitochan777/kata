class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    if self.head is not None:
      self.head.prev = new_node

    self.head = new_node

  def insertBefore(self, next_node, new_data):
    assert next_node is not None
    new_node = Node(new_data)
    if self.head == next_node:
      self.head = new_node

    new_node.prev = next_node.prev
    next_node.prev = new_node 
    new_node.next = next_node
    if new_node.prev is not None:
      new_node.prev.next = new_node

  def insertAfter(self, prev_node, new_data):
    assert prev_node is not None
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    new_node.prev = prev_node
    if new_node.next:
      new_node.next.prev = new_node

  def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
      return

    last = self.head
    while last.next:
      last = last.next

    last.next = new_node
    new_node.prev = last
    return

  def printList(self, node):
    ans = []
    while node:
      ans.append(str(node.data))
      node = node.next

    print(" ".join(ans))


dll = DoublyLinkedList()
dll.push(0)
ptr = dll.head

N = int(input())
S = input()
for i, c in enumerate(S):
  # dll.printList(dll.head)
  if c == "L":
    dll.insertBefore(ptr, i+1)
    ptr = ptr.prev
  else:
    dll.insertAfter(ptr, i+1)
    ptr = ptr.next

dll.printList(dll.head)