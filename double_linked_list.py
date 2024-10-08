class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.circular = False

    def append_node(self, node):
        self.tail.next = node
        node.previous = self.tail
        self.tail = node

    def append_in_the_beginning(self, node):
        self.head.previous = node
        node.next = self.head
        self.head = node

    def remove_node(self, num):
        current = self.head
        for _ in range(num):
            current = current.next

        previous_node = current.previous
        previous_node.next = current.next

    def reverse_list(self):
        current = self.tail
        while current:
            next = current.previous
            previous = current.next
            current = next
            current



    def print_list(self):
        current = self.head
        res = ''
        while current is not None:
            res += f"{current.value} -> "
            current = current.next
            if current is None:
               res += "Null"
               break
        print(res)

    def make_circular(self):
        self.tail.next = self.head
        self.head.previous = self.tail
        self.circular = True

    def pop_node(self):
        self.tail = self.tail.previous
        if self.circular:
            self.tail.next = self.head
            self.head.previous = self.tail
        else:
            self.tail.next = None

    def __repr__(self):
        self.print_list()
        return ""


head = Node(0)
dd = DoubleLinkedList(head)
for i in range(1, 5):
    dd.append_node(Node(i))
print(dd)
dd.reverse_list()
print(dd)
