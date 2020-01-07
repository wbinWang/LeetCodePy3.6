# 538 把二叉搜索树转换为累加树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    _sum = 0
    # 官方回溯
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root != None:
            self.convertBST(root.right)
            self._sum += root.val
            root.val = self._sum
            self.convertBST(root.left)
        return root

    # 自己的算法
    def convertBST2(self, root: TreeNode) -> TreeNode:
        self.handle(root, 0)
        return root

    # right_sum：该节点，右侧和
    def handle(self, root : TreeNode, right_sum : int) -> TreeNode:
        if root.right == None and right_sum == 0:
            # 最大值
            return root
        
        # 找到最大值
        # root.right.val += right_sum
        if root.right != None:
            root.right = self.handle(root.right, right_sum)
            # 找到最左侧
            first_left = root.right
            while first_left.left != None:
                first_left = first_left.left
            root.val += first_left.val
        else:
            root.val += right_sum
        
        if root.left != None:
            # root.left.val += root.val
            root.left = self.handle(root.left, root.val)

        return root

        

if __name__ == "__main__":
    t1 = TreeNode(1)

    t2 = TreeNode(3)

    t3 = TreeNode(2)
    t3.left = t1
    t3.right = t2

    ans = Solution().convertBST(t3)
    print(ans.val)