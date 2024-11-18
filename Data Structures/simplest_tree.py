class Tree:
    def __init__(self, data, ):
        self.data = data
        self.children = []

    def __str__(self, level=0):
        res = " " * level
        res += f"{str(self.data)}\n"
        for child in self.children:
            res += child.__str__(level + 1)
        return res

    def append_child(self, node):
        self.children.append(node)


tree = Tree("car")
sport = Tree('sport')
family = Tree('family')
tree.append_child(sport)
tree.append_child(family)
print(tree)
