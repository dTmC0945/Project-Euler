# open the textfile
with open('Text Files/Euler_018.txt') as file:
    lines = file.readlines()

mappedLines = list(map(lambda s: s.strip(), lines))




root = None


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def createTree(array):
    node_list = []
    global root

    for text in array:
        values = text.split()
        if len(values) == 1:
            root = Node(text)
        else:
            for numbers in values:
                node_list.append(Node(numbers))

    return node_list

print(createTree(mappedLines))