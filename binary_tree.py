# implement a binary tree

class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


node0 = Tree(1)
node1 = Tree(2)
node2 = Tree(3)

tree = node0
node0.left = node1
node0.right = node2
print(tree.key)
print(tree.left.key)
print(tree.right.key)

# recursively create binary tree from tuple


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = Tree(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Tree(data)
    return node


# inorder transversal of a binary tree

def inorder_transveral(node):
    if node is None:
        return []
    return(inorder_transveral(node.left) + [node.key] + inorder_transveral(node.right))


# preorder transveral of a binary tree
def preorder_transveral(node):
    if node is None:
        return []
    return([node.key] + preorder_transveral(node.left) + preorder_transveral(node.right))

# postorder transveral of a binary tree


def postorder_transveral(node):
    if node is None:
        return []
    return(postorder_transveral(node.left) + postorder_transveral(node.right) + [node.key])


print(inorder_transveral(tree))
print(postorder_transveral(tree))
print(preorder_transveral(tree))


# Height and size of binary tree

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
