# 617 合并二叉树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    
    # 迭代
    

if __name__ == "__main__":
    t1 = TreeNode(1)

    t2 = TreeNode(3)

    t3 = TreeNode(2)
    t3.left = t1
    t3.right = t2

    ans = Solution().mergeTrees(TreeNode(1), t3)
    print(ans.val, ans.left.val, ans.right.val)