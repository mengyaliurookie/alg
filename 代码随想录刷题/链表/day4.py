

# 24. 两两交换链表中的节点

topic="""
    给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 假设有三个节点先，记录三个节点，同时记录下一个节点，然后交换完，就移动两个位置
        dummyhead=ListNode(next=head)
        fir=dummyhead
        sec=dummyhead.next #这里sec就是head，head是可以为None的，所以thi可能会报错
        if not sec: return sec
        thi=sec.next
        while thi:
            # 记录下一个节点
            tem=thi.next
            # 第一个指向第三个
            fir.next=thi
            # 第三个指向第二个
            thi.next=sec
            # 第二个指向最新的
            sec.next=tem
            # 改变完之后，需要摆正第一第二第三的顺序
            if tem:
                # 如果tem不为空
                fir=sec
                sec=tem
                thi=sec.next
            else:
                # 如果为空，就不需要继续了
                break
        return dummyhead.next



# 19.删除链表的倒数第N个节点
topic="""
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 如果只遍历一遍的话，那么需要记录下倒数第n个节点的前一个节点
        # 可以使用类似快慢指针的思路，使得他们之间的距离保持为n，也就是fast-slow=n+1
        # 这样情况下可以使fast等于None
        # 还需要考虑要删除的节点如果是头结点的情况，所以需要一个虚拟头节点
        dummyhead = ListNode(next=head)
        fastind = 0
        slow, fast = dummyhead, dummyhead
        while fast:
            if fastind < n + 1:
                fastind += 1
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        # 此时slow指向的是要删除的节点的前一个节点
        if slow == dummyhead:
            dummyhead.next = dummyhead.next.next
        else:
            slow.next = slow.next.next
        return dummyhead.next


# 面试题 02.07. 链表相交
topic="""给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：



题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 先把一个遍历一遍，并把每个节点都记录下来，然后遍历另一个，并且判断当前节点在不在另一个集合中
        # 这样的空间复杂度比较高，因为需要保存历史访问的节点
        # seta=set()
        # ans=None
        # while headA:
        #     seta.add(headA)
        #     headA=headA.next
        # while headB:
        #     if headB in seta:
        #         ans=headB
        #         break
        #     else:
        #         headB=headB.next
        if not (headA and headB): return None
        ans = None
        a = headA
        b = headB
        aadd = 0
        badd = 0
        # 先从a开始遍历，然后接着遍历到b
        while a or b:
            # 当a为空的时候，需要换到b开始遍历
            if not a and aadd == 0:
                aadd += 1
                a = headB
            # 当b为空的时候，需要换到a开始遍历
            if not b and badd == 0:
                badd += 1
                b = headA
            if a == b:
                ans = a
                break
            else:
                a = a.next
                b = b.next

        return ans



# 142.环形链表II

topic="""给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

 

示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 

提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
 

进阶：你是否可以使用 O(1) 空间解决此题？"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针，并且差值在1，这样可以不会存在跳过的情况
        # 找到快慢指针第一次相遇的地方，然后另外两个指针，分别从开头和相遇点出发，再次相遇的地方就是环入口点
        # 如果不存在环的话，快慢指针不会相遇
        if not head: return None
        slow = head
        fast = head
        # 不满足条件的退出循环表示没有环
        while fast and fast.next:
            # 需要判断slow是不是等于fast
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        ans = None
        if fast and fast.next:
            # 开始从相遇点和起点出发
            # print("here")
            cur = head
            while slow != cur:
                cur = cur.next
                slow = slow.next
            ans = cur
        return ans



