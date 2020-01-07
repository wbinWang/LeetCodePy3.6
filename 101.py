# 101.对称二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    哈哈哈
    执行用时 :20 ms, 在所有 python3 提交中击败了100.00%的用户
    内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.45%的用户
    '''
    # 迭代
    def isSymmetric2(self, root : TreeNode) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        L = [root.left]
        R = [root.right]
        L1 = []
        R1 = []
        while True:
            arr_l = len(L)
            if arr_l == 0:
                break
            for i in range(0,arr_l):
                l = L[i]
                r = R[i]
                if l == None and r == None:
                    pass
                elif l != None and r != None:
                    if l.val == r.val:
                        L1.append(l.left)
                        L1.append(l.right)
                        R1.append(r.right)
                        R1.append(r.left)
                    else:
                        return False
                else:
                    return False
            L = L1
            R = R1
            L1 = []
            R1 = []
        return True

    # 递归，比迭代慢一些
    def isSymmetric(self, root : TreeNode) -> bool:
        return self.isMrror(root,root)

    def isMrror(self, l : TreeNode, r : TreeNode) -> bool:
        if l == None and r == None:
            return True
        elif l != None and r != None:
            if l.val != r.val:
                return False
            else:
                return self.isMrror(l.left,r.right) and self.isMrror(r.left,l.right)
        else:
            return False
        return True



if __name__ == "__main__":
    a = [1,2,2,3,4,4,3]
    a.reverse()
    print(a)
    # s = Solution()
    # # [1,2,2,null,3,null,3]
    
    # # [2,3,3,4,5,5,4,null,null,8,9,9,8]
    # l2 = TreeNode(3)
    # l2.right = TreeNode(4)

    # r2 = TreeNode(3)
    # r2.left = TreeNode(4)


    # l1 = TreeNode(2)
    # l1.left = l2
    
    # r1 = TreeNode(2)
    # r1.right = r2

    # root = TreeNode(1)
    # root.left = l1
    # root.right = r1

    # print(s.isSymmetric(root))