# tag: tree
# description
'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''

class Solution:

    def sameTree(self, tree1, tree2):
        # base cases
        # if both trees are empty, return True
        if not tree1 and not tree2:
            return True

        # if both trees are not empty and their values are the same,
        # check their left and right subtrees too
        if tree1 and tree2 and tree1.val == tree2.val:
            return (self.sameTree(tree1.left, tree2.left) and 
            self.sameTree(tree1.right, tree2.right))
          
        # if it is not the case, return False
        return False 



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is empty, it is a subtree of any tree
        if not subRoot:
            return True
        # if root is empty, it is not a subtree of any tree (because subRoot is not empty)
        if not root:
            return False

        # check if root and subRoot are the same tree
        if self.sameTree(root, subRoot):
            return True
        # if they are not the same tree, check if subRoot is a subtree of root's left or right subtree
        else:
            return (self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))
        