from queue_data_structure import Queue


class TreeNode:
    def __init__(self, data, left_child=[], right_child=[]):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child



class Tree:
    def __init__(self):
        self.nodes = []

    def append_child(self, child, parent):
        parent.append(child)

    def append_parent(self, child, parent):
        child.parents.append(parent)

    def traverse(self, root):
        if not root:
            return
        print(root.data)
        self.traverse(root.left_child)
        self.traverse(root.right_child)

    def reverse_traverse(self, root):
        if not root:
            return
        print(root.data)
        self.traverse(root.right_child)
        self.traverse(root.left_child)

    def in_order_traverse(self, root):
        if not root:
            return
        self.traverse(root.left_child)
        print(root.data)
        self.traverse(root.right_child)

    def search(self, root, data):
        if not root:
            return "Can't find node by value without root node."
        # using linked list as a queue
        queue = Queue()
        queue.enqueue(root)
        while not queue.empty:
            root = queue.dequeue()
            if root.data == data:
                return "Found it"
            if root.left_child:
                queue.enqueue(root.left_child)
            if root.right_child:
                queue.enqueue(root.right_child)
        return "Not found"

    def insert(self, root, node):
        if not root:
            root = node
        else:
            queue = Queue()
            queue.enqueue(root)
            while not queue.empty:
                root = queue.dequeue()
                if root.left_child:
                    queue.enqueue(root.left_child)
                else:
                    root.left_child = node
                if root.right_child:
                    queue.enqueue(root.right_child)
                else:
                    root.right_child = node

