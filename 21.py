# 21 合并两个有序列表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 迭代
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val > l2.val:
            tt = l2
            l2 = l1
            l1 = tt
            
        _l1 = l1
        _l2 = l2

        while _l1 != None and _l2 != None:
            if _l1.next == None:
                _l1.next = _l2
                break
            if _l2.val >= _l1.val and _l2.val <= _l1.next.val:
                t = _l2.next
                _l2.next = _l1.next
                _l1.next = _l2
                _l2 = t
            
            _l1 = _l1.next
        return l1

    # 递归
    def recursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.recursion(l1.next, l2)
            return l1
        else:
            l2.next = self.recursion(l2.next, l1)
            return l2


if __name__ == "__main__":
    s = Solution()
    n1_1 = ListNode(1)
    n1_2 = ListNode(2)
    n1_3 = ListNode(4)

    n1_2.next = n1_3
    n1_1.next = n1_2

    n2_1 = ListNode(1)
    n2_2 = ListNode(3)
    n2_3 = ListNode(4)

    n2_2.next = n2_3
    n2_1.next = n2_2

    next = s.recursion(n1_1,n2_1)
    while next:
        print(next.val)
        next = next.next