
# 150. 逆波兰表达式求值
topic="""
    给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

注意：

有效的算符为 '+'、'-'、'*' 和 '/' 。
每个操作数（运算对象）都可以是一个整数或者另一个表达式。
两个整数之间的除法总是 向零截断 。
表达式中不含除零运算。
输入是一个根据逆波兰表示法表示的算术表达式。
答案及所有中间计算结果可以用 32 位 整数表示。
 

示例 1：

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        alp={'+','-','*','/'}
        # 遇到数就入栈，遇到运算符就弹出栈顶两个元素，然后计算之后，再入栈
        stack=[]
        for al in tokens:
            if al not in alp:
                stack.append(int(al))
            else:
                if al=='+':
                    fir=stack.pop()
                    sec=stack.pop()
                    ans=int(sec)+int(fir)
                    stack.append(ans)
                elif al=="-":
                    fir=stack.pop()
                    sec=stack.pop()
                    ans=int(sec)-int(fir)
                    stack.append(ans)
                elif al=="*":
                    fir=stack.pop()
                    sec=stack.pop()
                    ans=int(sec)*int(fir)
                    stack.append(ans)
                else:
                    fir=stack.pop()
                    sec=stack.pop()
                    ans=int(int(sec)/int(fir))
                    stack.append(ans)
        return stack[0]

# 239. 滑动窗口最大值
topic="""
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = Mystack()
        ans = []
        for ind, val in enumerate(nums):
            if ind - k + 1 < 0:
                stack.push(val)
                continue
            # 先入栈
            stack.push(val)
            ans.append(stack.peak())
            # 弹出栈窗口左边的元素
            stack.pop(nums[ind - k + 1])
            # print(stack)
        return ans


class Mystack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
        else:
            while self.stack:
                if self.stack[0] < val:
                    self.stack.popleft()
                else:
                    break
            self.stack.appendleft(val)

    def pop(self, val):
        if self.stack[-1] == val:
            self.stack.pop()

    def peak(self):
        return self.stack[-1]

    def __str__(self):
        return f"Stack: {list(self.stack)}"

# 347.前 K 个高频元素
topic="""
    给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        dr = defaultdict(list)
        for i, v in d.items():
            dr[v].append(i)
        ans = []
        vl = list(dr.keys())
        vl.sort(reverse=True)
        for v in vl:
            ans.extend(dr[v])
            if len(ans) >= k:
                break
        return ans[:k]

