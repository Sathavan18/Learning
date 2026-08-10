# A tree is a hierarchical structure.
#             A
#           /   \
#          B     C
#         / \     \
#        D   E     F
# A is the root
# Lines connecting nodes are edges (\ or /).
# B is the parent of D and E. 
# D and E are also siblings since they share a parent.
# Useful Property: n nodes have n-1 edges.
# A leaf node has no children. D, E and F.
# The ancestors of F are C and A - anything above.
# The descendents of A are B,C,D,E and F - anything below.

# Subtrees:
# A subtree is a node plus everything underneat that node.
# # Subtree with B rooted, is B - D and E. F rooted is just F. 

# Depth vs Height:
# The depth is how far a node is from the root.
# The height is how far a node is from its deepest leaf.
# The height of the entire tree is the height of the root.
# Count the edges for both.

# Level:
# Level = depth + 1
# Some call root level 0 so clarify in interviews. 

# Binary Tree:
# A tree where each node can have at most two children.
# Full Binary Tree: Every node has either 0 or 2 children.
# Perfect Binary Tree: Every internal node has exactly 2 children and all leaves are at the same depth.
# Complete Binary Tree: Every level is completely filled except possible the final level, 
# and the final level is filled from left to right.
# Balanced Binary Tree: At every node, the heights of its left and right subtrees differ by at most 1.

# How Trees Exist in Python:
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = TreeNode(10)
node.left = TreeNode(20)
node.right = TreeNode(30)
#node
#│
#├── val   = 10
#├── left  = 20
#└── right = 30