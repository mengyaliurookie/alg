
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


