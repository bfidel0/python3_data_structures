# BST tree check along with min and max recursive

from operator import truediv


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    is_bst_node = (is_bst_l and is_bst_r and (
        max_l is None is node.key > max_l) and (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return is_bst_node, min_key, max_key


# Storing K,V pairs using BST setup

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# Insert into BST recursivly

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

# Find a node in BST recusive


def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if node < node.key:
        return find(node.left, key)
    if node > node.key:
        return find(node.right, key)


# update a node in a BST

def update(node, key, value):
    target = find(node, key)
    try:
        if target is not None:
            target.value = value
    except:
        print("node not found")


# list all nodes in a BST

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


# Balanced binary tree

def is_balanced(node):
    if node is None:
        return True, 0
    bal_l, height_l = is_balanced(node.left)
    bal_r, height_r = is_balanced(node.right)
    balanced = bal_l and bal_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height


# Create balanced BST from a sorted list of K, V pairs recursive

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    # terminating condition
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    return root

# Balance an Unbalanced BST
# Would just entail remaking the tree with said K, V pairs
# Would be expensive to do this everytime however


def balance_bst(node):
    return make_balanced_bst(list_all(node))
