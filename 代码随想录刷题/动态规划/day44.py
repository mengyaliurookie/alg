# 1143.最长公共子序列
topic="""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

 

示例 1：

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
"""
# 这是动态规划的一般解法，但是会超时
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]表示以text1[i]结尾的和以text2[j]结尾的最长公共子序列的长度
        # 递推公式：
        # dp[i][j]=if text1[i]==text2[j]:dp[i][j]=0
        # for k in range(i):
        #   for l in range(j):
        #       dp[i][j]=max(dp[i][j],dp[k][l]+1)
        n1=len(text1)
        n2=len(text2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        ans=0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=0
                    for k in range(i):
                        for l in range(j):
                            dp[i][j]=max(dp[i][j],dp[k][l]+1)
                ans=max(ans,dp[i][j])
        return ans

# 修改了dp数组的定义，这样就不用重复的去遍历之前的每一种情况了，只需要保证dp[i][j]依赖的dp[i-1][j-1],dp[i-1][j],dp[i][j-1]已经计算出来了
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]表示以text1[i]结尾的和以text2[j]结尾子字符串中的的最长公共子序列的长度
        # 递推公式：
        # dp[i][j]=if text1[i]==text2[j]:max(dp[i-1][j-1]+1,dp[i-1][j],dp[i][j-1])
        # else:dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        # for k in range(i):
        #   for l in range(j):
        #       dp[i][j]=max(dp[i][j],dp[k][l]+1)
        n1=len(text1)
        n2=len(text2)
        dp=[[0]*(n2) for _ in range(n1)]
        # 初始化
        ans=0
        for i in range(n1):
            if text2[0] in text1[:i+1]:
                dp[i][0]=1
                ans=max(ans,dp[i][0])
        for j in range(n2):
            if text1[0] in text2[:j+1]:
                dp[0][j]=1
                ans=max(ans,dp[0][j])
        # print(dp)
        for i in range(1,n1):
            for j in range(1,n2):
                if text1[i]==text2[j]:
                    dp[i][j]=max(dp[i-1][j-1]+1,dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                ans=max(ans,dp[i][j])
        # print(dp)
        return ans

# 1035.不相交的线
topic="""
在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足：

 nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。

 

示例 1：


输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。 
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。
示例 2：

输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
输出：3
示例 3：

输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
输出：2
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j]表示以nums1[i]和以nums2[j]为结尾的子数组中不相交线的最大连线数
        # 递推公式：
        # if nums1[i]==nums2[j]:
        #   dp[i][j]=dp[i-1][j-1]+1
        # else:
        #   dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        n1=len(nums1)
        n2=len(nums2)
        dp=[[0]*n2 for _ in range(n1)]
        for i in range(n1):
            if nums2[0] in nums1[:i+1]:
                dp[i][0]=1
        for j in range(n2):
            if nums1[0] in nums2[:j+1]:
                dp[0][j]=1
        for i in range(1,n1):
            for j in range(1,n2):
                if nums1[i]==nums2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n1-1][n2-1]


# 53. 最大子序和
topic="""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
"""
# 贪心方法求解
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 只要局部和小于零，那么就不会是最大连续子数组的一部分
        psum=nums[0]
        first=0
        sec=0
        res=max(psum,float('-inf'))
        n=len(nums)
        while sec<n:
            if psum<0:
                sec+=1
                first=sec
                if sec<n:
                    psum=nums[sec]
                res=max(res,psum)
            else:
                sec+=1
                if sec<n:
                    psum+=nums[sec]
                res=max(res,psum)
        return res
        
# 动态规划求解
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划的解法，可以采用一分为二的，然后合并的
        # dp[i]表示以nums[i]结尾的连续子数组的最大和
        # 递推公式：
        # dp[i]=max(dp[i-1]+nums[i],nums[i])
        # 
        dp=[0]*len(nums)
        dp[0]=nums[0]
        ans=dp[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            ans=max(ans,dp[i])
        return ans

# 392.判断子序列
topic="""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢：

特别感谢 @pbrother 添加此问题并且创建所有测试用例。

 

示例 1：

输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：

输入：s = "axc", t = "ahbgdc"
输出：false
"""
# 直接查表解法
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns=len(s)
        nt=len(t)
        # 可以转化为子问题
        # 感觉10亿级别的，应该得先把t分析一下，每个字符存成一个哈希，索引存成value，然后查表
        dic=defaultdict(list)
        for i,v in enumerate(t):
            dic[v].append(i)
        print(dic)
        lastindex=-1
        ans=True
        for vs in s:
            if dic[vs]:
                tem=lastindex
                for i in dic[vs]:
                    if i>lastindex:
                        lastindex=i
                        break
                if tem==lastindex:
                    ans=False
                    break
            else:
                ans=False
                break
        return ans


# 记忆化搜索的解法
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns=len(s)
        nt=len(t)
        # 可以转化为子问题
        @cache
        def dfs(i,j):
            if i==nt and j<ns:
                # 当t遍历完成时，但是s没有遍历完成，则表示不存在
                return False
            if j==ns:
                # 当s遍历完成时，就表示所有都在
                return True
            # 找到第一个和j相等的i
            return dfs(i+1,j+1) if s[j]==t[i] else dfs(i+1,j)
        return dfs(0,0)

# 动态规划，二维解法
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns=len(s)
        nt=len(t)
        if ns==0:return True
        if nt==0:return False
        # 改成动态规划的解法
        # dp[i][j]表示s[:i+1]是不是t[:j+1]的子序列
        # 递推公式是：
        # dp[i][j]=if s[i]==t[j]: dp[i][j]=dp[i-1][j-1]
        # else: dp[i][j]=dp[i][j-1]
        dp=[[False]*ns for _ in range(nt)]
        for i in range(nt):
            if s[0] in t[:i+1]:
                dp[i][0]=True
        for i in range(1,nt):
            for j in range(1,ns):
                if s[j]==t[i]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[nt-1][ns-1]
# 一维数组的方式
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if ns == 0:
            return True

        dp = [False] * ns
        for i in range(nt):  # 👈 统一从 i=0 开始
        # 逆序更新，避免覆盖
            for j in range(ns - 1, -1, -1):  # 👈 j 从 ns-1 到 0
                if j == 0:
                    if s[0] == t[i]:
                        dp[0] = True
                else:
                    if s[j] == t[i]:
                        dp[j] = dp[j - 1]

        return dp[ns - 1]