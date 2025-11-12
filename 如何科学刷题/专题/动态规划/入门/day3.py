
# 2320 统计放置房子的方式数
topic="""
一条街道上共有 n * 2 个 地块 ，街道的两侧各有 n 个地块。每一边的地块都按从 1 到 n 编号。每个地块上都可以放置一所房子。
现要求街道同一侧不能存在两所房子相邻的情况，请你计算并返回放置房屋的方式数目。由于答案可能很大，需要对 109 + 7 取余后再返回。
注意，如果一所房子放置在这条街某一侧上的第 i 个地块，不影响在另一侧的第 i 个地块放置房子。 
示例 1：
输入：
n = 1
输出：
4
解释：
可能的放置方式：
1. 所有地块都不放置房子。
2. 一所房子放在街道的某一侧。
3. 一所房子放在街道的另一侧。
4. 放置两所房子，街道两侧各放置一所。
示例 2：
输入：
n = 2
输出：
9
解释：
如上图所示，共有 9 种可能的放置方式。
"""

# 递归加记忆化搜索的方式
class Solution:
    def countHousePlacements(self, n: int) -> int:
        # 两侧的房子是没有关系的，所以可以直接相乘各自的情况
        # 因此转化为一侧不能相邻的情况
        # 当第一个位置不放的时候，就是n-1个位置的子问题了
        # 当第一个位置放的时候，第二个位置就不能放了，所以就转化为n-2个位置的子问题了
        MOD=1000000007
        @cache
        def dfs(n):
            if n<=0:
                return 0
            if n==2:
                return 3
            if n==1:
                return 2
            return dfs(n-1)%MOD+dfs(n-2)%MOD
        return dfs(n)**2%MOD

# 转化为动态规划的方式
class Solution:
    def countHousePlacements(self, n: int) -> int:
        # 两侧的房子是没有关系的，所以可以直接相乘各自的情况
        # 因此转化为一侧不能相邻的情况
        # 当第一个位置不放的时候，就是n-1个位置的子问题了
        # 当第一个位置放的时候，第二个位置就不能放了，所以就转化为n-2个位置的子问题了
        MOD=1000000007
        # dp[n]表示街道一侧有n个地块可以防止的房子的方式数目
        # 递推公式为
        # dp[n]=dp[n-1]+dp[n-2]
        if n==1:return 2**2
        # dp=[0]*(n+1)
        f=[1,2]
        # dp[0]=1
        # dp[1]=2
        for i in range(2,n+1):
            # dp[i]=dp[i-1]%MOD+dp[i-2]%MOD
            f[0],f[1]=f[1],(f[0]+f[1])%MOD
        return f[-1]**2%MOD
        # return dp[n]**2%MOD

        # @cache
        # def dfs(n):
        #     if n<=0:
        #         return 0
        #     if n==2:
        #         return 3
        #     if n==1:
        #         return 2
        #     return dfs(n-1)%MOD+dfs(n-2)%MOD
        # return dfs(n)**2%MOD