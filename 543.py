# 543 二叉树的直径

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self._max = 0

        def depth(note : TreeNode):
            if note == None:
                return -1
            left = 1 + depth(note.left)
            right = 1 + depth(note.right)
            self._max = max(self._max, left + right)
            return max(left , right)
        depth(root)

        return self._max



if __name__ == "__main__":
    t1 = TreeNode(1)

    t2 = TreeNode(3)

    t3 = TreeNode(2)
    t3.left = t1
    t3.right = t2

    ans = Solution().diameterOfBinaryTree(t3)
    print(ans)