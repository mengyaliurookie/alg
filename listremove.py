# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 以防头节点是val
        tem = ListNode(0, head)
        # 先需要排除head都是val的情况
        while head:
            # 此时head不为None，是可以有next的
            if head.val == val:
                tem.next = head.next
                # 此时需要更新head
                head = head.next
            else:
                break
        # 到这里tem指向的一定不是等于val的
        # 但是head可能是None
        if head is None:
            return None
        else:
            # 此时需要删除中间是val的节点
            pre = head
            head = head.next
            while head:
                if head.val == val:
                    pre.next = head.next
                    head = head.next
                else:
                    head = head.next
                    pre = pre.next
        head = tem.next

        return head

