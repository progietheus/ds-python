# Python does not have built-in tree support. Normally at an interview, you'd be given the following implementation for binary tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# For n-nary trees:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
