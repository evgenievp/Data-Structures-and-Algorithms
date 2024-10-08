class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.circular = False
        self.value_for_print_circular_list = 100

    def append_node(self, node):
        head = self.head
        while head.next:
            head = head.next
        head.next = node
        self.tail = head.next

    def pop_node(self):
        head = self.head
        while head.next:
            head = head.next
        head.next = None

    def remove_node(self, num):
        head = self.head
        for i in range(num - 1):
            head = head.next
        node_for_remove = head.next
        head.next = node_for_remove.next

    def make_circular(self):
        self.circular = True
        self.tail.next = self.head

    def append_in_the_beginning(self, value):
        node = Node(value)
        node.next = head
        self.head = node

    def get_node(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current


    def remove_from_the_beginning(self):
        head = self.head.next
        self.head = head

    def print_circular_list(self):
        head = self.head
        res = ''
        for i in range(self.value_for_print_circular_list):
            res += f"{head.value} -> "
            head = head.next
        print(res)

    def reverse_list(self):
        current = self.head
        previous = None
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


head = Node(0)
ll = LinkedList(head)
for i in range(1, 6):
    node = Node(i)
    ll.append_node(node)
ll.reverse_list()
ll.print_list()

