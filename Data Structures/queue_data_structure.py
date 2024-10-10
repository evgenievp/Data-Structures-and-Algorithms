class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, data=None):
        self.head = data
        self.tail = data
        self.length = 0
        self.empty = True

    def enqueue(self, node):
        if self.empty:
            self.empty = False
        if not self.tail:
            self.tail = node
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        if self.length > 0:
            self.head = self.head.next
            self.length -= 1
        if self.length == 0:
            self.empty = True

    def __repr__(self):
        res = ''
        current = self.head
        while current.next != self.tail:
            res += f"{current.data} -> "
            current = current.next
        res += "None"
        return res

