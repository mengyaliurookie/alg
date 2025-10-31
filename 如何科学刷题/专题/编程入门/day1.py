
# 2235 两整数相加
topic="""
给你两个整数 num1 和 num2，返回这两个整数的和。
 

示例 1：

输入：num1 = 12, num2 = 5
输出：17
解释：num1 是 12，num2 是 5 ，它们的和是 12 + 5 = 17 ，因此返回 17 。
示例 2：

输入：num1 = -10, num2 = 4
输出：-6
解释：num1 + num2 = -6 ，因此返回 -6 。
 

提示：

-100 <= num1, num2 <= 100
 

"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


# 2469 温度转换
topic="""
给你一个四舍五入到两位小数的非负浮点数 celsius 来表示温度，以 摄氏度（Celsius）为单位。

你需要将摄氏度转换为 开氏度（Kelvin）和 华氏度（Fahrenheit），并以数组 ans = [kelvin, fahrenheit] 的形式返回结果。

返回数组 ans 。与实际答案误差不超过 10-5 的会视为正确答案。

注意：

开氏度 = 摄氏度 + 273.15
华氏度 = 摄氏度 * 1.80 + 32.00
 

示例 1 ：

输入：celsius = 36.50
输出：[309.65000,97.70000]
解释：36.50 摄氏度：转换为开氏度是 309.65 ，转换为华氏度是 97.70 。
示例 2 ：

输入：celsius = 122.11
输出：[395.26000,251.79800]
解释：122.11 摄氏度：转换为开氏度是 395.26 ，转换为华氏度是 251.798 。
 

提示：

0 <= celsius <= 1000
"""

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15,celsius*1.8+32]

# 2413 最小偶倍数
topic="""
给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。
 

示例 1：

输入：n = 5
输出：10
解释：5 和 2 的最小公倍数是 10 。
示例 2：

输入：n = 6
输出：6
解释：6 和 2 的最小公倍数是 6 。注意数字会是它自身的倍数。
 

提示：

1 <= n <= 150
"""
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return 2*n if n%2==1 else n

# 2236 判断根结点是否等于子结点之和
topic="""
给你一个 二叉树 的根结点 root，该二叉树由恰好 3 个结点组成：根结点、左子结点和右子结点。

如果根结点值等于两个子结点值之和，返回 true ，否则返回 false 。

 

示例 1：


输入：root = [10,4,6]
输出：true
解释：根结点、左子结点和右子结点的值分别是 10 、4 和 6 。
由于 10 等于 4 + 6 ，因此返回 true 。
示例 2：


输入：root = [5,3,1]
输出：false
解释：根结点、左子结点和右子结点的值分别是 5 、3 和 1 。
由于 5 不等于 3 + 1 ，因此返回 false 。
 

提示：

树只包含根结点、左子结点和右子结点
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val==(root.left.val+root.right.val)

# 1486 数组异或操作
topic="""
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。

 

示例 1：

输入：n = 5, start = 0
输出：8
解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     "^" 为按位异或 XOR 运算符。
示例 2：

输入：n = 4, start = 3
输出：8
解释：数组 nums 为 [3, 5, 7, 9]，其中 (3 ^ 5 ^ 7 ^ 9) = 8.
示例 3：

输入：n = 1, start = 7
输出：7
示例 4：

输入：n = 10, start = 5
输出：2
 

提示：

1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=0
        for i in range(n):
            res=res^(start+2*i)
        return res

# 1512 好数对的数目
topic="""
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。

 

示例 1：

输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
示例 2：

输入：nums = [1,1,1,1]
输出：6
解释：数组中的每组数字都是好数对
示例 3：

输入：nums = [1,2,3]
输出：0
 

提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=Counter()
        for v in nums:
            cnt[v]+=1
        res=0
        for k,v in cnt.items():
            if v>=2:
                res+=v*(v-1)/2
        return int(res)

# 1534 统计好三元组
topic="""
给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。

如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
其中 |x| 表示 x 的绝对值。

返回 好三元组的数量 。

 

示例 1：

输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
输出：4
解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。
示例 2：

输入：arr = [1,1,2,2,3], a = 0, b = 0, c = 1
输出：0
解释：不存在满足所有条件的三元组。
 

提示：

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000
"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length=len(arr)
        ans=0
        for i in range(length-2):
            for j in range(i+1,length-1):
                for k in range(j+1,length):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        ans+=1
        return ans

# 709 转换成小写字母
topic="""
给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

 

示例 1：

输入：s = "Hello"
输出："hello"
示例 2：

输入：s = "here"
输出："here"
示例 3：

输入：s = "LOVELY"
输出："lovely"
 

提示：

1 <= s.length <= 100
s 由 ASCII 字符集中的可打印字符组成
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        li=[]
        for i in s:
            if 64<ord(i)<91:
                li.append(chr(ord(i)+32))
            else:
                li.append(i)
        return ''.join(li)

# 258 各位相加
topic="""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

 

示例 1:

输入: num = 38
输出: 2 
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。
示例 2:

输入: num = 0
输出: 0
 

提示：

0 <= num <= 231 - 1
 

进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while not 0 <= num <= 9:
            num = self.getsum(num)
        return num

    def getsum(self, num: int) -> int:
        ans = 0
        while num:
            ans += num % 10
            num = num // 10
        return ans

# 1281 整数的各位积和之差
topic="""
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

 

示例 1：

输入：n = 234
输出：15 
解释：
各位数之积 = 2 * 3 * 4 = 24 
各位数之和 = 2 + 3 + 4 = 9 
结果 = 24 - 9 = 15
示例 2：

输入：n = 4421
输出：21
解释： 
各位数之积 = 4 * 4 * 2 * 1 = 32 
各位数之和 = 4 + 4 + 2 + 1 = 11 
结果 = 32 - 11 = 21
 

提示：

1 <= n <= 10^5
"""

class Solution:
    ans=[]
    def subtractProductAndSum(self, n: int) -> int:
        self.ans=[]
        self.getw(n)
        print(self.ans)
        mul=1
        sm=0
        for i in self.ans:
            mul*=i
            sm+=i
        return mul-sm
    def getw(self,n:int)->None:
        while n:
            self.ans.append(n%10)
            n//=10

# 231 2的幂
topic="""
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

 

示例 1：

输入：n = 1
输出：true
解释：20 = 1
示例 2：

输入：n = 16
输出：true
解释：24 = 16
示例 3：

输入：n = 3
输出：false
 

提示：

-231 <= n <= 231 - 1
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:return False
        while n:
            if n==1: return True
            if n%2:
                return False
            n//=2
        return True

# 326 3的幂
topic="""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

 

示例 1：

输入：n = 27
输出：true
示例 2：

输入：n = 0
输出：false
示例 3：

输入：n = 9
输出：true
示例 4：

输入：n = 45
输出：false
 

提示：

-231 <= n <= 231 - 1
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:return False
        while n>1:
            if n%3:
                # 不能被3整除
                return False
            n//=3
        return True

# 263 丑数
topic="""
丑数 就是只包含质因数 2、3 和 5 的 正 整数。

给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

 

示例 1：

输入：n = 6
输出：true
解释：6 = 2 × 3
示例 2：

输入：n = 1
输出：true
解释：1 没有质因数。
示例 3：

输入：n = 14
输出：false
解释：14 不是丑数，因为它包含了另外一个质因数 7 。
 

提示：

-231 <= n <= 231 - 1
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:return False
        if n==1:return True
        while n>=2:
            if n%2==0 or n%3==0 or n%5==0:
                if n%2==0:
                    n//=2
                if n==1:
                    return True
                if n%3==0:
                    n//=3
                if n==1:
                    return True
                if n%5==0:
                    n//=5
                if n==1:
                    return True
            else:
                return False

# 1470 重新排列数组
topic="""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

 

示例 1：

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
示例 2：

输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]
示例 3：

输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]
 

提示：

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        for i in range(n):
            nexti=i+n
            ans.append(nums[i])
            ans.append(nums[nexti])
        return ans


# 867 转置矩阵
topic="""
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：matrix = [[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""


