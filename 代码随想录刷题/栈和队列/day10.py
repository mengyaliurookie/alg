
# 232.用栈实现队列
topic="""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：

你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 

示例 1：

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stak2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        n = len(self.stack1)
        for i in range(n):
            self.stak2.append(self.stack1.pop())
        ans = None
        if self.stak2:
            ans = self.stak2.pop()
        m = len(self.stak2)
        for j in range(m):
            self.stack1.append(self.stak2.pop())
        return ans

    def peek(self) -> int:
        n = len(self.stack1)
        for i in range(n):
            self.stak2.append(self.stack1.pop())
        ans = None
        if self.stak2:
            ans = self.stak2[-1]
        m = len(self.stak2)
        for j in range(m):
            self.stack1.append(self.stak2.pop())
        return ans

    def empty(self) -> bool:
        ans = None
        if self.stack1:
            ans = False
        else:
            ans = True
        return ans

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# 225. 用队列实现栈
topic="""
    请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
 

注意：

你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
 

示例：

输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
"""

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        # 只能用append和popleft

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        n = len(self.queue1)
        for i in range(n - 1):
            self.queue2.append(self.queue1.popleft())
        ans = None
        if self.queue1:
            ans = self.queue1.popleft()
        m = len(self.queue2)
        for j in range(m):
            self.queue1.append(self.queue2.popleft())
        return ans

    def top(self) -> int:
        n = len(self.queue1)
        for i in range(n - 1):
            self.queue2.append(self.queue1.popleft())
        ans = None
        if self.queue1:
            ans = self.queue1.popleft()
            self.queue2.append(ans)
        m = len(self.queue2)
        for j in range(m):
            self.queue1.append(self.queue2.popleft())
        return ans

    def empty(self) -> bool:
        if self.queue1:
            return False
        else:
            return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# 20. 有效的括号
topic="""
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：

输入：s = "()"

输出：true
"""
class Solution:
    def isValid(self, s: str) -> bool:
      stack=[]
      # 括号匹配应该使用栈，遇到左括号就入栈，遇到右括号就出栈
      # 如果栈顶元素和右括号不匹配，就返回False
      # 当遍历完s之后，栈不为空，也返回False
      # 需要先存储一个字典
      dic={'(':')','[':']','{':'}'}
      dicr={')':'(',']':'[','}':'{'}
      for i in s:
        if i in dic:
          stack.append(i)
        else:
          if len(stack)==0:
            return False
          if dicr[i]==stack[-1]:
            stack.pop()
          else:
            return False
      if len(stack)!=0:
        return False
      return True

# 1047. 删除字符串中的所有相邻重复项
topic="""
    给出由小写字母组成的字符串 s，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 s 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

 

示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
 

提示：

1 <= s.length <= 105
s 仅由小写英文字母组成。
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 如果栈为空则入栈，如果栈顶元素与当前元素不同则入栈，否则则出栈
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
