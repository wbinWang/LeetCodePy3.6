# 160 相交链表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 先不考虑空间复杂度O(1)
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        d = {}
        _a = headA
        while _a != None:
            _a_id = id(_a)
            d[_a_id] = 1
            _a = _a.next
        _b = headB
        while _b != None:
            _b_id = id(_b)
            if _b_id in d:
                return _b
            _b = _b.next
        return None

    # 空间复杂度为常数，双指针法
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        p1 = headA
        p1_null_count = 0
        p2 = headB
        p2_null_count = 0
        while True:
            if id(p1) == id(p2):
                return p1
            if p1 == None:
                if p1_null_count == 0:
                    p1_null_count = 1
                    p1 = headB
                else:
                    return None
            else:
                p1 = p1.next

            if p2 == None:
                if p2_null_count == 0:
                    p2_null_count = 1
                    p2 = headA
                else:
                    return None
            else:
                p2 = p2.next
            


if __name__ == "__main__":
    pass