

# 203.移除链表元素
job='''给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
 

示例 1：


输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
示例 2：

输入：head = [], val = 1
输出：[]'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dimmyhead = ListNode(0, head)
        pre = dimmyhead
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next

        return dimmyhead.next

# 707.设计链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummyhead = ListNode()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummyhead.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummyhead.next = ListNode(val, self.dummyhead.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummyhead
        for _ in range(self.size):
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # 需要获取index指向的节点的前一个结点
        if not (index < 0 or index > self.size):
            cur = self.dummyhead
            for _ in range(index):
                cur = cur.next
            # 此时cur指向的是index的前一个
            cur.next = ListNode(val, cur.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # 还是需要遍历到index节点的前一个节点
        if not (index < 0 or index >= self.size):
            #
            cur = self.dummyhead
            for _ in range(index):
                cur = cur.next
            # 此时cur指向的是index的前一个节点
            cur.next = cur.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# 206.反转链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        first = None
        second = head
        # 每次必须处理第一个节点
        while second:
            # 记录下一个节点
            tem = second.next
            # 使得第二个节点直向前一个节点
            second.next = first
            # 移动第一个节点到第二个节点
            first = second
            # 移动第二个节点到下一个节点
            second = tem
        # 最后退出循环的时候，second是为None的，所以他的前一个节点才是反转之后的头结点
        return first

