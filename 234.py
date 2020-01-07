# 234 回文链表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 将链表 -> 数组 (貌似没人这么干)
    def isPalindrome2(self, head: ListNode) -> bool:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        arr_len = len(arr)
        if arr_len == 0:
            return True
        for i in range(0, int(arr_len / 2)):
            l = arr[i]
            r = arr[arr_len - 1 - i]
            if l != r:
                return False
        return True

    # 快慢指针，找到中心点，然后再依次判断
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        left_half = None
        slow = head
        quick = head
        while quick != None and quick.next != None:
            quick = quick.next.next

            first = slow
            slow = slow.next
            first.next = left_half
            left_half = first
            

        # 偶数个
        if quick != None:
            slow = slow.next

        while left_half != None:
            if left_half.val != slow.val:
                return False
            left_half = left_half.next
            slow = slow.next

        return True


if __name__ == "__main__":
    l1 = ListNode(5)

    l2 = ListNode(4)
    l2.next = l1

    l3 = ListNode(4)
    l3.next = l2

    l4 = ListNode(5)
    l4.next = l3
    
    print(Solution().isPalindrome(l4))