#  141 环形链表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 哈希表的做法
    def hasCycle2(self, head: ListNode) -> bool:
        d = {}
        while head != None:
            _id = id(head)
            if _id in d:
                return True
            else:
                head = head.next
                d[_id] = 1
        return False


    # 快慢指针
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        slow = head
        quick = head.next
        while slow != None and quick != None:
            if id(slow) == id(quick):
                return True
            else:
                slow = slow.next
                if quick.next == None:
                    return False
                else:
                    quick = quick.next.next
        return False

if __name__ == "__main__":
    l1 = ListNode(0)

    l2 = ListNode(1)
    l2.next = l1

    l3 = ListNode(2)
    l3.next = l2

    l1.next = l3

    print(Solution().hasCycle(l3))