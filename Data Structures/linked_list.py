class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        if head:
            self.head = head
            self.tail = head
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0
        self.circular = False
        self.value_for_print_circular_list = 100

    def append_node(self, node):
        if self.length > 0:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def pop_node(self):
        self.length -= 1
        head = self.head
        while head.next != self.tail:
            head = head.next
        head.next = None

    def remove_node(self, num):
        self.length -= 1
        head = self.head
        for i in range(num - 1):
            head = head.next
        node_for_remove = head.next
        head.next = node_for_remove.next

    def make_circular(self):
        self.circular = True
        self.tail.next = self.head
        return "Linked list is Circular from now."

    def append_in_the_beginning(self, value):
        self.length += 1
        node = Node(value)
        node.next = self.head
        self.head = node

    def get_node(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current

    def remove_from_the_beginning(self):
        self.head -= 1
        head = self.head.next
        self.head = head

    def print_circular_list(self):
        head = self.head
        res = ''
        for _ in range(self.value_for_print_circular_list):
            res += f"{head.value} -> "
            head = head.next
        print(res)

    def reverse_list(self):
        current = self.head.next
        previous = self.head
        while current is not None:
            next_node = current.next
            current.next = previous

            self.head = current
            previous = current
            current = next_node

    def print_list(self):
        if not self.circular:
            head = self.head
            res = ''
            while head:
                res += f"{head.value} -> "
                if head.next is None:
                    res += "Null"
                    break
                head = head.next

            print(res)
        else:
            self.print_circular_list()

