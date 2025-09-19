# 647. 回文子串
topic="""
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

 

示例 1：

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""
# 双指针的解法
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 新使用双指针的写法
        n=len(s)
        ans=0
        lastis=False
        for i in range(n):
            # 这种好像能获取到奇数个数的
            fir,sec=i,i
            # 指定双指针，然后向外扩散
            # 直到某个指针到达终点（即开头或者结尾）
            while not (fir==-1 or sec==n):
                if fir==sec:
                    # 只有一个字符
                    ans+=1
                    lastis=True
                elif sec-fir==1:
                    # 中间没有字符
                    if s[sec]==s[fir]:
                        ans+=1
                        lastis=True
                    else:
                        lastis=False
                else:
                    # 中间有字符
                    # 如果上一个是True
                    if s[sec]==s[fir]:
                        if lastis:
                            ans+=1
                    else:
                        lastis=False
                fir-=1
                sec+=1
        
        for j in range(1,n):
            # 这样可以来处理偶数的
            fir=j-1
            sec=j
            while not (fir==-1 or sec==n):
                if fir==sec:
                    # 只有一个字符
                    ans+=1
                    lastis=True
                elif sec-fir==1:
                    # 中间没有字符
                    if s[sec]==s[fir]:
                        ans+=1
                        lastis=True
                    else:
                        lastis=False
                else:
                    # 中间有字符
                    # 如果上一个是True
                    if s[sec]==s[fir]:
                        if lastis:
                            ans+=1
                    else:
                        lastis=False
                fir-=1
                sec+=1
        
        return ans


# 动态规划的形式
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 再使用动态规划的方式
        # dp[i][j]表示以i和j为边界的子区间字符串是不是回文子串
        # 递推公式是，当s[i]==s[j]的时候，需要判断i+1,j-1是不是回文子串，是的话那dp[i][j]也是
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        # 还需要初始化一下
        # 就是当i=n-1的时候和j=0的时候
        ans=0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if i==j:
                        dp[i][j]=True
                        ans+=1
                    elif j-i==1:
                        dp[i][j]=True
                        ans+=1
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j]=True
                            ans+=1
        return ans


# 516.最长回文子序列
topic="""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
"""
# 记忆化搜索的方式
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 回文字符串，如果把字符串反转一下，是和原来的是相等的
        # 所以可以转化为求两个字符串的最长公共子序列
        # 算了，先试一下直接用递归的方式求解吧
        # 从头和尾开始可以选或者不选，当i，j指向的字符相等的时候，就加2
        # 不相等，就选择分别选i，j两个不同的字符的时候的大的子问题
        n=len(s)
        @cache
        def dfs(i,j):
            # print(f"i: {i}")
            # print(f"j: {j}")
            if i==j:
                return 1
            if i>j:
                return 0
            return dfs(i+1,j-1)+2 if s[i]==s[j] else max(dfs(i+1,j),dfs(i,j-1))
        return dfs(0,n-1)

# 动态规划的求解形式
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 回文字符串，如果把字符串反转一下，是和原来的是相等的
        # 所以可以转化为求两个字符串的最长公共子序列
        # 算了，先试一下直接用递归的方式求解吧
        # 从头和尾开始可以选或者不选，当i，j指向的字符相等的时候，就加2
        # 不相等，就选择分别选i，j两个不同的字符的时候的大的子问题
        n=len(s)
        # 改成动态规划的形式，进行求解
        # dp[i][j]中i和j表示在s[i:j+1]中间的最大回文子串长度
        # 递推公式是
        dp=[[0]*n for _ in range(n)]
        # 初始化
        for i in range(n):
            dp[i][i]=1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                
                    if s[i]==s[j]:
                        dp[i][j]=dp[i+1][j-1]+2
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        # print(dp)
        return dp[0][-1]


# 739. 每日温度
topic="""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

 

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]
"""
# 单调栈的实现
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 先初始化结果集合
        ans=[0]*len(temperatures)
        # 需要一个数据结构来保存还没有找到下一个更高温度的ind
        # 先入的要后出，所以需要栈
        q=deque()
        # 同时要去除可以直接判断的
        for i,v in enumerate(temperatures):
            # 如果队列为空，或者队列的头部元素大于当前元素，就直接入队
            # print(q)
            if not q or temperatures[q[-1]]>=v:
                q.append(i)
            else:
                while q and temperatures[q[-1]]<v:
                    ind=q.pop()
                    ans[ind]=i-ind
                q.append(i)
        return ans

# 496.下一个更大元素 I
topic="""
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

 

示例 1：

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
示例 2：

输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
"""
# 也是用单调栈的方式，先把整个nums2上的元素的下一个更大元素都求出来，然后存储到一个字典中
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 可以利用上一道题的解法
        # 把nums2中的所有元素的得下一个最大元素都存储起来，然后查表
        dic=defaultdict(int)
        stack=[]
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                v=stack.pop()
                dic[v]=nums2[i]
            stack.append(nums2[i])
        ans=[-1]*len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in dic:
                ans[i]=dic[nums1[i]]
        return ans


