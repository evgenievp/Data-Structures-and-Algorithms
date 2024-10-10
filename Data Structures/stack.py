class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, node):
        if self.tail:
            node.previous = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
            self.head.previous = None
        self.length += 1

    def pop_element(self):
        if self.tail:
            self.tail = self.tail.previous
            self.length -= 1

    def __repr__(self):
        current = self.tail
        res = ''
        while current is not None:
            res += f"{current.data} -> "
            current = current.previous
        res += "Null"
        return res


ss = Stack()
for i in range(10):
    ss.add_node(Node(i))
print(ss)
for i in range(10):
    ss.pop_element()
    print(ss)