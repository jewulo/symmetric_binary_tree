# This is a sample Python script.
from typing import Optional


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# https://youtube.com/shorts/JodJZjJtECE


# node structure
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def sym(root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.key != root2.key:
            return False

        return sym(root1.left, root2.right) and \
            sym(root1.right, root2.left)

    return sym(root, root)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(3)
    t1.left.right = TreeNode(4)
    t1.right.left = TreeNode(4)
    t1.right.right = TreeNode(3)
    print("Symmetric" if isSymmetric(t1) is True else "Not Symmetric")

    t2 = TreeNode(1)
    t2.left = TreeNode(8)
    t2.right = TreeNode(7)
    t2.left.left = TreeNode(3)
    t2.left.right = TreeNode(6)
    t2.right.left = TreeNode(4)
    t2.right.right = TreeNode(9)
    print("Symmetric" if isSymmetric(t2) is True else "Not Symmetric")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
