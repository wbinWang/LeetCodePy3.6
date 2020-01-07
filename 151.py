# 151 mini栈

class ListNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

# 使用双向链表
class MinStack:

    head = None
    last = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        
    def push(self, x: int) -> None:
        item = ListNode(x)
        if self.head == None:
            self.head = item
            self.last = self.head
        else:
            self.last.right = item
            self.last = item
        
        return None

    def pop(self) -> None:
        if self.head == None:
            return None
        if self.last.left == None:
            self.head = None
            self.last = None
            return None
        self.last = self.last.left
        self.last.right = None


    def top(self) -> int:
        if self.head == None:
            return 0
        return self.head.val

    def getMin(self) -> int:
        _h = self.head
        if _h == None:
            return 0
        _min = _h.val
        while _h != None:
            _min = min(_min, _h.val)
            print("_min",_min)
            _h = _h.right
        return _min


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())