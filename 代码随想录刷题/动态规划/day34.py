
# 62.不同路径
topic="""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp数组表示到达某个节点总共有多少条路径
        # 而到达i，j的方式有从它的上方（如果存在的话）或者它的左方（如果存在的话）
        # 所以递推公式为
        # dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # 因为上面的公式要求i和j必须大于0，所以需要先处理i，j等于0的边界条件
        dp=[[0]*n for _ in range(m)]
        # i等于0的时候，只有一个来源可以达到，就是从左边
        dp[0][0]=1
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]
        # j等于0的时候，只有一个来源可以到达，就是从上边
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]
        # 然后就是递推公式
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp数组表示到达某个节点总共有多少条路径
        # 而到达i，j的方式有从它的上方（如果存在的话）或者它的左方（如果存在的话）
        # 所以递推公式为
        # dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # 因为上面的公式要求i和j必须大于0，所以需要先处理i，j等于0的边界条件
        dp=[1]*(n)
        # dp=[[0]*n for _ in range(m)]
        # i等于0的时候，只有一个来源可以达到，就是从左边
        # dp[0][0]=1
        # for j in range(1,n):
            # dp[0][j]=dp[0][j-1]
        # j等于0的时候，只有一个来源可以到达，就是从上边
        # for i in range(1,m):
            # dp[i][0]=dp[i-1][0]
        # 然后就是递推公式
        # for i in range(1,m):
            # print(dp)
            # for j in range(1,n):
                # dp[i][j]=dp[i-1][j]+dp[i][j-1]

        # 改成一维的动态数组的话，
        # dp[j]=dp[j](表示来自上面的)+dp[j-1](表示来自左边的)
        for i in range(1,m):    
            for j in range(1,n):
                dp[j]=dp[j]+dp[j-1]
        # return dp[m-1][n-1]
        return dp[n-1]


        return dp[m-1][n-1]

# 63. 不同路径 II
topic="""
给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。

网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。

返回机器人能够到达右下角的不同路径数量。

测试用例保证答案小于等于 2 * 109。


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1
 

提示：

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1
 

"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 和不同路径那道题思路差不多，只是需要加一个当前节点是不是通的判断
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1*(1-obstacleGrid[0][0])
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]*(1-obstacleGrid[0][j])
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]*(1-obstacleGrid[i][0])
        # 递推
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])*(1-obstacleGrid[i][j])
        return dp[m-1][n-1]

# 一维数组
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 和不同路径那道题思路差不多，只是需要加一个当前节点是不是通的判断
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        # dp=[[0]*n for _ in range(m)]
        dp=[0]*n
        # dp[0][0]=1*(1-obstacleGrid[0][0])
        dp[0]=1*(1-obstacleGrid[0][0])
        for j in range(1,n):
            dp[j]=dp[j-1]*(1-obstacleGrid[0][j])
        # for j in range(1,n):
        #     dp[0][j]=dp[0][j-1]*(1-obstacleGrid[0][j])
        # for i in range(1,m):
        #     dp[i][0]=dp[i-1][0]*(1-obstacleGrid[i][0])
        # 递推
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j]=(dp[i-1][j]+dp[i][j-1])*(1-obstacleGrid[i][j])
        for i in range(1,m):
            dp[0]=dp[0]*(1-obstacleGrid[i][0])
            for j in range(1,n):
                dp[j]=(dp[j-1]+dp[j])*(1-obstacleGrid[i][j])
        # return dp[m-1][n-1]
        return dp[n-1]

# 343. 整数拆分
topic="""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。

 

示例 1:

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
 

提示:

2 <= n <= 58
"""

# 这里是递归加缓存的记忆化搜索版本
class Solution:
    def integerBreak(self, n: int) -> int:
        # 拆分为子问题拆出一个1，那么剩下n-1，k-1个数
        # 拆出一个2，那么剩下n-2，k-1个数
        # 。。。
        # 拆出一个n-k+1，那么剩下k-1个数
        # k从2到n
        if n==2:return 1
        if n==3:return 2
        if n==4:return 4
        @cache
        def dfs(n):
            if n<=1:
                return 1
            maxv=float('-inf')
            for i in range(1,n+1):
                r=i*dfs(n-i)
                maxv=max(r,maxv)
            return maxv
        return dfs(n)

# 这是根据递归版本改成的动态规划版本
class Solution:
    def integerBreak(self, n: int) -> int:
        # 拆分为子问题拆出一个1，那么剩下n-1，k-1个数
        # 拆出一个2，那么剩下n-2，k-1个数
        # 。。。
        # 拆出一个n-k+1，那么剩下k-1个数
        # k从2到n

        # 转化为动态规划的形式
        # dp[n]=max(dp[n-1],2*dp[n-2],3*dp[n-3]......)
        if n==2:return 1
        if n==3:return 2
        if n==4:return 4
        dp=[1]*(n+1)
        dp[1],dp[2],dp[3],dp[4]=1,2,3,4
        for i in range(5,n+1):
            maxv=float('-inf')
            # print('i: ',i)
            for j in range(1,i):
                # print('j: ',j)
                maxv=max(j*dp[i-j],maxv)
            dp[i]=maxv
        return dp[n]
        # if n==2:return 1
        # if n==3:return 2
        # if n==4:return 4
        # @cache
        # def dfs(n):
        #     if n<=1:
        #         return 1
        #     maxv=float('-inf')
        #     for i in range(1,n+1):
        #         r=i*dfs(n-i)
        #         maxv=max(r,maxv)
        #     return maxv
        # return dfs(n)


# 96.不同的二叉搜索树
topic="""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

 

示例 1：


输入：n = 3
输出：5
示例 2：

输入：n = 1
输出：1
 

提示：

1 <= n <= 19
"""
class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i]: 表示由 i 个节点组成，能构成多少种不同的二叉搜索树
        dp = [0] * (n + 1)
        
        # 初始化
        dp[0] = 1 # 空树是一种情况
        
        # 递推公式: dp[i] = sum(dp[j-1] * dp[i-j]) for j in 1...i
        # i 从 1 遍历到 n
        for i in range(1, n + 1):
            # j 从 1 遍历到 i, 代表当前根节点的序号
            for j in range(1, i + 1):
                # 左子树节点数 j-1, 右子树节点数 i-j
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[n]

# 这是一个递归加缓存的记忆化搜索版本
class Solution:
    def numTrees(self, n: int) -> int:
        # 怎么转化为一个子问题呢，假设根节点是1，那么只能是右子树是2到n能构成多少种
        # 根节点是2，那么就是左子树1，右子树3到n
        # 根节点是3，那么左节点是1到2构成的乘以4到n构成的

        @cache
        def dfs(start,end):
            if (end-start)==0:
                return 1
            if (end-start)==1:
                return 2
            ans=0
            for i in range(start,end+1):
                if i==start:
                    left=1
                    right=dfs(start+1,end)
                elif i==end:
                    left=dfs(start,end-1)
                    right=1
                else:
                    left=dfs(start,i-1)
                    right=dfs(i+1,end)
                ans+=left*right
            return ans
        return dfs(1,n)
            




