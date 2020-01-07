# 206 翻转链表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    ans = None

    # 迭代2
    def reverseList(self, head: ListNode) -> ListNode:
        tail = None
        while head != None:
            first = head
            head = head.next
            first.next = tail
            tail = first
        return tail

    # 迭代1
    def reverseList3(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        tail = head
        head = head.next
        tail.next = None
        while head != None:
            first = head
            head = head.next
            first.next = tail
            tail = first
        return tail

    # 递归
    def reverseList2(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        self._reverseList(head)
        return self.ans

    def _reverseList(self, head: ListNode) -> ListNode:
        if head.next == None:
            self.ans = head
            return head
        # 第一个节点
        first = head
        # 剩余节点
        x = self._reverseList(head.next)
        x.next = first
        first.next = None
        return first


if __name__ == "__main__":
    n1 = ListNode(1)

    n2 = ListNode(2)
    n2.next = n1

    n3 = ListNode(3)
    n3.next = n2

    n4 = ListNode(4)
    n4.next = n3

    r = Solution().reverseList(n4)
    while r != None:
        print("-----",r.val)
        r = r.next