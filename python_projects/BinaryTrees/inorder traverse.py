class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
res = []
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        if root.val == None:
            pass
        else:
            res.append(root.val)
        # now recur on right child
        printInorder(root.right)

    return res

# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(None)
    root.right = Node(2)
    root.right.left = Node(3)

    # Function call
    print
    "\nInorder traversal of binary tree is"
    print(printInorder(root))


