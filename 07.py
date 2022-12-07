class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
        self.traversed = False
        self.size = 0

    def __str__(self) -> str:
        return self.data["name"]

    def addNode(self, obj):
        self.children.append(obj)


def recursive_print(node, level = 0):
    level += 1
    if node:
        print("  " * level, end="")
        print("- " + node.data["name"], end=" ")
        if "size" in node.data:
            print(node.size, end=" ")
        else:
            print(" (dir) ", end="")
            print(node.size, end=" ")
        print()

        for child in node.children:
            recursive_print(child, level)

def recursive_count(node):
    if node:
        #print(node.data["name"])
        if (node.size > 0 and node.size < 100000):
            global total_size
            total_size += node.size

        for child in node.children:
            recursive_count(child)


def add_size_to_parents(node, size):
    if node:
        node.size += size
        add_size_to_parents(node.parent, size)


with open('input7.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    root = Node({"name": "/"})
    pointer = root

    total_size = 0

    for line in lines:
        line = line.strip()
        if line.startswith("$ cd"):
            dir = line.split(" ").pop()

            if dir == "/":
                pointer = root
            elif dir == "..":
                pointer = pointer.parent
            else:
                for node in pointer.children:
                    if (node.data["name"] and node.data["name"] == dir):
                        pointer = node

        elif line.startswith("$ ls"):
            pass
        else:
            file = line.split(" ")
            if file[0] == "dir":
                node = Node({"name": file[1]})
                node.parent = pointer
                pointer.children.append(node)
            else:
                node = Node({"name": file[1], "size": file[0]})
                node.parent = pointer
                pointer.children.append(node)
                add_size_to_parents(pointer, int(file[0]))

    #recursive_print(root)
    recursive_count(root)
    print(total_size)
    