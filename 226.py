# 226 翻转二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 官方的递归
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.right = l
        root.left = r
        return root


    #  自己的递归
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        ans = self.rep(root.left, root.right)
        root.left = ans[0]
        root.right = ans[1]
        return root

    
    def rep(self, left: TreeNode, right: TreeNode) -> []:
        left1 = None
        right1 = None

        if left != None and right != None:
            ans1 = self.rep(left.left, right.right)
            ans2 = self.rep(left.right, right.left)

            left1 = TreeNode(right.val)
            left1.left = ans1[0]
            left1.right = ans2[0]
            right1 = TreeNode(left.val)
            right1.left = ans2[1]
            right1.right = ans1[1]

        elif left != None:
            right1 = TreeNode(left.val)
            ans1 = self.rep(left.left, None)
            ans2 = self.rep(left.right, None)
            right1.left = ans2[1]
            right1.right = ans1[1]

        elif right != None:
            left1 = TreeNode(right.val)
            ans1 = self.rep(None, right.right)
            ans2 = self.rep(None, right.left)
            left1.left = ans1[0]
            left1.right = ans2[0]

        return [left1, right1]
        


if __name__ == "__main__":
    pass