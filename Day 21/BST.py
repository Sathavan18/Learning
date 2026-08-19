# values in left subtree < node, values in right > node.
# for Leetcode, no duplicates allowed.
def searchBST(root, target):
    if root is None:
            return False
    if target == root.val:
        return True
    if target < root.val:
        return searchBST(root.left, target)
    return searchBST(root.right, target)
# Inorder traversal of a valid BST gives values in ascending order.
#lower = float('-inf')
#upper = float('inf')

class Solution(object):
    def isValidBST(self, root):
        def dfs(node, lower, upper):
            if node is None:
                 return True
            if node.val <= lower or node.val >= upper:
                return False
            left = dfs(node.left, lower,node.val)
            right = dfs(node.right,node.val, upper)
            return left and right
        return dfs(root, float('-inf'), float('inf'))