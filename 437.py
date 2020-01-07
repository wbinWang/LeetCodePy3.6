# 437 路径总和（三）
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    need_sum = 0

    # 1 递归可行
    # 但是
    # 执行用时 :588 ms, 在所有 Python3 提交中击败了57.51%的用户
    # 内存消耗 :33.3 MB, 在所有 Python3 提交中击败了9.56%的用户
    # 貌似讲解用的也是这个方法
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.need_sum = sum
        return self._pathSum(root, [self.need_sum])

    # sums 里面包含 所需的数字
    def _pathSum(self, root: TreeNode, sums: [int]) -> int:
        # 基线条件
        if root == None:
            return 0
        res = 0
        for i in range(0, len(sums)):
            n = sums[i]
            if n == root.val:
                res += 1
                sums[i] = 0
            else:
                sums[i] = n - root.val
        return res + self._pathSum(root.left, sums + [self.need_sum]) + self._pathSum(root.right, sums + [self.need_sum])


if __name__ == "__main__":
    pass
    # [10,5,-3,3,2,null,11,5,-10,null,1]