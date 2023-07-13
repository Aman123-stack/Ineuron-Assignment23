q1>def calculate_depth(preorder):
    stack = []
    depth = -1  # Start with -1 to account for the root node
    for char in preorder:
        if char == 'n':
            stack.append(char)  # Push 'n' onto the stack
            depth += 1  # Increment depth
        elif char == 'l':
            stack.pop()  # Pop 'n' from the stack
            if not stack:  # If the stack is empty, we have reached the leaf node
                depth = 0  # Reset the depth to 0
    return depth

# Test the function with the given example
preorder = "nlnll"
depth = calculate_depth(preorder)
print("Depth of the binary tree:", depth)



q2>class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def left_view(root):
    if root is None:
        return

    queue = []  # Create a queue for level order traversal
    queue.append(root)
    left_view_nodes = []  # List to store the leftmost nodes at each level

    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)

        # Traverse all the nodes at the current level
        for i in range(level_size):
            node = queue.pop(0)

            # If it's the leftmost node, print it
            if i == 0:
                left_view_nodes.append(node.data)

            # Add the left and right child of the current node to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Print the left view nodes
    for node_value in left_view_nodes:
        print(node_value, end=" ")


# Constructing the binary tree given in the example
root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7)

# Print the left view of the binary tree
print("Left View of Binary Tree:")
left_view(root)



q3>class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def right_view(root):
    if root is None:
        return

    queue = []  # Create a queue for level order traversal
    queue.append(root)
    right_view_nodes = []  # List to store the rightmost nodes at each level

    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)

        # Traverse all the nodes at the current level
        for i in range(level_size):
            node = queue.pop(0)

            # If it's the rightmost node, print it
            if i == level_size - 1:
                right_view_nodes.append(node.data)

            # Add the left and right child of the current node to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Print the right view nodes
    for node_value in right_view_nodes:
        print(node_value, end=" ")


# Constructing the binary tree given in the example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

# Print the right view of the binary tree
print("Right View of Binary Tree:")
right_view(root)




q4>from collections import defaultdict


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def bottom_view(root):
    if root is None:
        return

    # Map to store nodes at each horizontal distance
    node_map = defaultdict(Node)

    # Queue for level order traversal
    queue = []
    queue.append((root, 0))  # Tuple containing node and its horizontal distance

    # Perform level order traversal
    while queue:
        node, hd = queue.pop(0)

        # Update the node for the corresponding horizontal distance
        node_map[hd] = node

        # Enqueue the left and right child of the current node
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Print the bottom view nodes from the map
    for key in sorted(node_map.keys()):
        print(node_map[key].data, end=" ")


# Constructing the binary tree given in the example
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# Print the bottom view of the binary tree
print("Bottom View of Binary Tree:")
bottom_view(root)
