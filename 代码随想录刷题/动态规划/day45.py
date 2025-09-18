# 115.不同的子序列
topic="""
给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。

测试用例保证结果在 32 位有符号整数范围内。

 

示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
babgbag
babgbag
babgbag
babgbag
babgbag
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls=len(s)
        lt=len(t)
        # 先使用双指针的方式来求解
        # 感觉比较直观一点
        # sind=0
        # tind=0
        # while True:
        #     # 先找到t[tind]第一次出现的位置
        #     while s[sind]!=t[tind]:
        #         sind+=1
            # 此时sind指向的和tind指向的是第一次相等的位置
            # 还需要找到第二个字符第一次相等的地方，这中间s中有多少个第一个字符，就有多少种可能。






        # 这种比较两个的，一般先用一个二维的dp数组来
        # dp[i][j]表示s[:i+1]中t[:j+1]出现的个数
        # 递推公式
        # if s[i]==t[j] 可以选择或者不选择
        # 那么dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        # s[i]!=t[j]
        # 此时应该是s[:i]中t[:j+1]出现的个数
        # 初始化
        
        # 先用递归的方式求解一下，是比较符合思考的方式的

        dp=[[0]*lt for _ in range(ls)]
        # # 初始化
        if s[0]==t[0]:dp[0][0]=1
        for i in range(1,ls):
            if t[0]==s[i]:
                dp[i][0]=dp[i-1][0]+1
            else:
                dp[i][0]=dp[i-1][0]
        for i in range(1,ls):
            for j in range(1,lt):
                if s[i]==t[j]:
                    # 相等的时候，可以选择或者不选
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        # print(dp)
        return dp[ls-1][lt-1]
# 改成一维数组，注意初始化的时候的意义。
# dp[0]表示的是t[0]在s[:i+1]中出现的次数
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls=len(s)
        lt=len(t)
        # 先使用双指针的方式来求解
        # 感觉比较直观一点
        # sind=0
        # tind=0
        # while True:
        #     # 先找到t[tind]第一次出现的位置
        #     while s[sind]!=t[tind]:
        #         sind+=1
            # 此时sind指向的和tind指向的是第一次相等的位置
            # 还需要找到第二个字符第一次相等的地方，这中间s中有多少个第一个字符，就有多少种可能。






        # 这种比较两个的，一般先用一个二维的dp数组来
        # dp[i][j]表示s[:i+1]中t[:j+1]出现的个数
        # 递推公式
        # if s[i]==t[j] 可以选择或者不选择
        # 那么dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        # s[i]!=t[j]
        # 此时应该是s[:i]中t[:j+1]出现的个数
        # 初始化
        
        # 先用递归的方式求解一下，是比较符合思考的方式的

        dp=[0]*lt
        # # 初始化
        if s[0]==t[0]:dp[0]=1
        # for i in range(1,ls):
        #     if t[0]==s[i]:
        #         dp[0]=dp[0]+1
        for i in range(1, ls):
            # 逆序更新 j（避免覆盖）
            for j in range(lt - 1, 0, -1):
                if s[i] == t[j]:
                    dp[j] += dp[j - 1]
            # 更新 dp[0]
            if s[i] == t[0]:
                dp[0] += 1
        # print(dp)
        return dp[lt-1]

# 583. 两个字符串的删除操作
topic="""
给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。

每步 可以删除任意一个字符串中的一个字符。

 

示例 1：

输入: word1 = "sea", word2 = "eat"
输出: 2
解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
示例  2:

输入：word1 = "leetcode", word2 = "etco"
输出：4
 

提示：

1 <= word1.length, word2.length <= 500
word1 和 word2 只包含小写英文字母
"""
# 记忆化搜索的方式求解的
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1=len(word1)
        w2=len(word2)

        # 先用递归的方式求解一下
        @cache
        def dfs(i,j):
            if i==w1 and j!=w2:
                return w2-j
            if i!=w1 and j==w2:
                return w1-i
            if w1==i and w2==j:
                return 0
            return dfs(i+1,j+1) if word1[i]==word2[j] else min(dfs(i,j+1),dfs(i+1,j))+1
        return dfs(0,0)


# 改成二维动态规划的形式
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # w1=len(word1)
        # w2=len(word2)

        # # 先用递归的方式求解一下
        # @cache
        # def dfs(i,j):
        #     if i==w1 and j!=w2:
        #         return w2-j
        #     if i!=w1 and j==w2:
        #         return w1-i
        #     if w1==i and w2==j:
        #         return 0
        #     return dfs(i+1,j+1) if word1[i]==word2[j] else min(dfs(i,j+1),dfs(i+1,j))+1
        # return dfs(0,0)

        # 相等的时候可以不操作
        # 不相等的时候，可以选择删除一个
        # dp[i][j] 表示使得word1[:i+1]和word2[:j+1]相同所需的最小步数
        # 递推公式
        # 当word1[i]==word2[j]的时候，不操作就是最小的dp[i][j]=dp[i-1][j-1]
        # 当word1[i]!=word2[j]的时候，可以选择删除任意一个min(dp[i-1][j],dp[i][j-1])+1
        w1=len(word1)
        w2=len(word2)
        dp=[[0]*w1 for _ in range(w2)]
        # # 初始化
        # if word1[0]!=word2[0]:dp[0][0]=2
        for i in range(w1):
            if word2[0] in word1[:i+1]:
                dp[0][i]=i
            else:
                # 
                dp[0][i]=i+2
        for j in range(w2):
            if word1[0] in word2[:j+1]:
                dp[j][0]=j
            else:
                dp[j][0]=j+2
        for i in range(1,w2):
            for j in range(1,w1):
                if word1[j]==word2[i]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]


# 72. 编辑距离
topic="""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""
# 记忆化搜索的方式，相比上一道两个字符串的，好像是多了一些操作
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 
        w1=len(word1)
        w2=len(word2)
        @cache
        def dfs(i,j):
            if i==w1 and j!=w2:
                # 此时直接插入w2剩下的字符
                return w2-j
            if i!=w1 and j==w2:
                # 此时直接删除w1剩下的字符
                return w1-i
            if i==w1 and j==w2:
                # 此时直接返回0就可以了
                return 0
            return dfs(i+1,j+1) if word1[i]==word2[j] else min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1))+1
        return dfs(0,0)

# 动态规划的版本
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 改成动态规划的解法
        # dp[i][j]表示将word1[:i+1]改成word2[:j+1]所需要做的最少操作
        # 递推公式
        w1=len(word1)
        w2=len(word2)
        if w1==0:return w2
        if w2==0:return w1
        dp=[[0]*w2 for _ in range(w1)]
        # 初始化
        # 当word2只有一个字符的时候，只要word2在word1[:i+1]中，直接保留一个，删除剩下的就可以
        # 不在的时候，直接替换一个，然后删除剩下的就可以
        for i in range(w1):
            if word2[0] in word1[:i+1]:
                dp[i][0]=i
            else:
                dp[i][0]=i+1
        # 当word1只有一个字符的时候，只要word1在word2[:j+1]中，直接保留一个，然后剩下的都插入
        # 不在就都插入
        for j in range(w2):
            if word1[0] in word2[:j+1]:
                dp[0][j]=j
            else:
                dp[0][j]=j+1
        for i in range(1,w1):
            for j in range(1,w2):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
        return dp[-1][-1]
