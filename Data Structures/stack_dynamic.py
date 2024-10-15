class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DynamicStack:
    def __init__(self):
        self.head = None
        self.max_length = 10
        self.current_length = 0

    def append_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.length_control("plus")

    def pop_node(self):
        if self.length_control("pop"):
            next_node = self.head
            current = None
            while next_node.next is not None:
                next_node = next_node.next
                if next_node.next is None:
                    break
                current = next_node
            if current:
                current.next = None
                return
            else:
                self.head = None
        else:
            return

    def length_control(self, do):
        if do == "plus" and self.current_length == self.max_length:
            self.max_length *= 2
            self.current_length += 1
            # In C language here we call malloc function with another memory for our new nodes.
            # Here this is not needed.
            return True
        if do == "pop" and self.current_length == 0:
            return False
        if do == "plus" and self.current_length < self.max_length:
            self.current_length += 1
            return True
        elif do == "pop" and self.current_length > 0:
            self.current_length -= 1
            return True

    def reverse_stack(self):
        if self.current_length > 1:
            current = None
            next_node = self.head
            while next_node is not None:
                new_node = next_node.next
                next_node.next = current
                current = next_node
                next_node = new_node
        self.head = current

    def print_stack(self):
        current = self.head
        if current is None:
            return "Null"
        res = f"{current.value} -> "
        while current.next is not None:
            current = current.next
            res += f"{current.value} -> "
        res += "Null"
        return res


ss = DynamicStack()
for i in range(11):
    ss.append_node(i)
print(ss.print_stack())
ss.reverse_stack()
print(ss.print_stack())

