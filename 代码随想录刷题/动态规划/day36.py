# 1049.最后一块石头的重量II
topic="""
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

 

示例 1：

输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
示例 2：

输入：stones = [31,26,33,21,40]
输出：5
"""

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 转化为将stones分组，是的两组的差值最小
        # 这个两组差值最小，可以把整个石头进行求和，然后除以2，得到bag
        # 将bag尽量装满，那么就可以得到最小剩下的重量
        # 价值等于重量的话，当价值最大的时候，背包就是塞的最满的时候
        s=sum(stones)
        bag=s//2
        n=len(stones)
        dp=[0]*(bag+1)
        # 初始化
        for i in range(bag+1):
            if i>=stones[0]:
                dp[i]=stones[0]
        # 
        for i in range(1,n):
            for j in range(bag,stones[i]-1,-1):
                dp[j]=max(dp[j],dp[j-stones[i]]+stones[i])
        # print(dp)
        return abs(s-dp[bag]-dp[bag])



# 494.目标和
topic="""
给你一个非负整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

 

示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1
"""
# 下面是通过递归加上缓存的记忆化搜索方式
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 转化为子问题，nums中的某个数加到target中和不加到target中两种，
        # 先用递归加缓存的记忆化搜索方式，再改成动态规划
        s=sum(nums)
        # ans=0
        n=len(nums)
        @cache
        def dfs(i,add):
            if i==n and target==add:
                # nonlocal ans
                # ans+=1
                return 1
            if i>=n:return 0
            # 选当前元素为负数
            left=dfs(i+1,add-2*nums[i])
            # 选当前元素为正数
            right=dfs(i+1,add)
            return left+right
        ans=dfs(0,s)
        return ans

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)  # 计算nums的总和
        if abs(target) > total_sum:
            return 0  # 此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0  # 此时没有方案
        target_sum = (target + total_sum) // 2  # 目标和
        dp = [0] * (target_sum + 1)  # 创建动态规划数组，初始化为0
        dp[0] = 1  # 当目标和为0时，只有一种方案，即什么都不选
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] += dp[j - num]  # 状态转移方程，累加不同选择方式的数量
        return dp[target_sum]  # 返回达到目标和的方案数



# 474.一和零
topic="""
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

 

示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
"""
# 记忆化搜索版本的
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 还是选和不选的问题
        le=len(strs)
        def getzo(st):
            a,b=0,0
            for i in st:
                if i=='0':a+=1
                else:b+=1
            return a,b
        @cache
        def dfs(i,m,n):
            if m<0 or n<0:
                # 说明选多了，需要减去1
                return -1
            if i==le:
                return 0
            o,l=getzo(strs[i])
            left=dfs(i+1,m-o,n-l)+1
            right=dfs(i+1,m,n)
            return max(left,right)
        return dfs(0,m,n)

# 动态规划版本的
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 还是选和不选的问题
        le=len(strs)
        def getzo(st):
            a,b=0,0
            for i in st:
                if i=='0':a+=1
                else:b+=1
            return a,b
        # dp数组的含义是，根据递归函数的参数i表示物品选还是不选
        # m和n表示背包的容量
        # 当装满一个背包的时候就停止
        # dp[i][j]表示当背包容量m为i，n为j的时候装满背包最多的子集个数
        # 递推公式是dp[i][j]=max(dp[i][j],dp[i-o][j-l]+1)
        # 初始条件是
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in strs:
            o,l=getzo(i)
            for mm in range(m,o-1,-1):
                for nn in range(n,l-1,-1):
                    dp[mm][nn]=max(dp[mm][nn],dp[mm-o][nn-l]+1)
        print(dp)
        return dp[m][n]
        # @cache
        # def dfs(i,m,n):
        #     if m<0 or n<0:
        #         # 说明选多了，需要减去1
        #         return -1
        #     if i==le:
        #         return 0
        #     o,l=getzo(strs[i])
        #     left=dfs(i+1,m-o,n-l)+1
        #     right=dfs(i+1,m,n)
        #     return max(left,right)
        # return dfs(0,m,n)



