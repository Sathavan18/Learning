# DFS - Depth First Search
# Go all the way down left, backtrack and go right, backtrack
#        1
#       / \
#      2   3
#     / \
#    4   5
# Preorder DFS: process node before ecploring either subtree
'''
def dfs(node):
    if node == None:
        return
    print(node.val)
    dfs(node.left)
    dfs(node.right)
'''
# Print order: 1,2,4,5,3
# Inorder: node processed in between the two recursive calls
'''
    dfs(node.left)
    print(node.val)
    dfs(node.right)
'''
# Print order: 4,2,5,1,3
# Postorder: node processed after both subtrees
'''
    dfs(node.left)
    dfs(node.right)
    print(node.val)
'''
# Print order: 4,5,2,3,1
# Implementing traversals:
'''
def traversal(node):
    if node is None:
        return
    # three operations go here
'''
# Max Depth
'''
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left,right)
'''
# The max number of calls is the height of tree.
# So Space complexity is O(h) and Time is O(n).
# SameTree:
'''
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right # asks is left true and right true
'''