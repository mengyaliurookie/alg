# 完全背包的理论基础

# 有N件物品和一个最多能背重量为W的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品都有无限个（也就是可以放入背包多次），求解将哪些物品装入背包里物品价值总和最大。
# 完全背包和01背包问题唯一不同的地方就是，每种物品有无限件。
topic="""
52. 携带研究材料（第七期模拟笔试）
题目描述
小明是一位科学家，他需要参加一场重要的国际科学大会，以展示自己的最新研究成果。他需要带一些研究材料，但是他的行李箱空间有限。这些研究材料包括实验设备、文献资料和实验样本等等，它们各自占据不同的重量，并且具有不同的价值。

小明的行李箱所能承担的总重量是有限的，问小明应该如何抉择，才能携带最大价值的研究材料，每种研究材料可以选择无数次，并且可以重复选择。

输入描述
第一行包含两个整数，n，v，分别表示研究材料的种类和行李所能承担的总重量 

接下来包含 n 行，每行两个整数 wi 和 vi，代表第 i 种研究材料的重量和价值

输出描述
输出一个整数，表示最大价值。
输入示例
4 5
1 2
2 4
3 4
4 5
输出示例
10
提示信息
第一种材料选择五次，可以达到最大值。

数据范围：

1 <= n <= 10000;
1 <= v <= 10000;
1 <= wi, vi <= 10^9.
"""
import sys

def main():
    n,v=map(int,sys.stdin.readline().strip().split())
    w=[0]*n
    value=[0]*n
    for i in range(n):
        w[i],value[i]=map(int,sys.stdin.readline().strip().split())
    dp=[[0]*(v+1) for _ in range(n)]
    # 递推公式
    # dp[i][j]=max(dp[i-1][j],dp[i][j-w[i]]+value[i])
    # 初始化
    for i in range(v+1):
        if i>=w[0]:dp[0][i]=dp[0][i-w[0]]+value[0]
    for i in range(1,n):
        for j in range(1,v+1):
            if j>=w[i]:
                dp[i][j]=max(dp[i-1][j],dp[i][j-w[i]]+value[i])
            else:
                dp[i][j]=dp[i-1][j]
    # print(dp)
    print(dp[n-1][v])

# if __name__=="__main__":
#     main()

# 518.零钱兑换II
topic="""
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。 

题目数据保证结果符合 32 位带符号整数。

 

示例 1：

输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2：

输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3 。
示例 3：

输入：amount = 10, coins = [10] 
输出：1
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j]表示有i+1种硬币数，可以凑成j金额数的组合数
        # 递推公式：
        # dp[i][j]=dp[i-1][j](不选i代表的硬币最多可以组成的数)+dp[i][j-coins[i]](选)
        # 初始化
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for i in range(amount+1):
            if i%coins[0]==0:dp[0][i]=1
        # 当amount等于0的时候，无论多少种硬币，都有一种选择，就是都不选
        for i in range(n):
            dp[i][0]=1
        for i in range(1,n):
            for j in range(1,amount+1):
                if j>=coins[i]:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n-1][amount]
        

# 377. 组合总和 Ⅳ
topic="""
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

 

示例 1：

输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
示例 2：

输入：nums = [9], target = 3
输出：0
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp[i][j]：总和为 j，且最后一个数是 nums[i] 的排列数
        dp = [[0] * (target + 1) for _ in range(n)]
        
        # 初始化：只选一个数的情况
        for i in range(n):
            if nums[i] <= target:
                dp[i][nums[i]] = 1  # 只选自己，一种方案
        
        # 填表：按目标和从小到大
        for j in range(1, target + 1):
            for i in range(n):  # 枚举最后一个数是 nums[i]
                if j < nums[i]:
                    continue
                # 如果最后一个是 nums[i]，那么前面的和是 j - nums[i]
                # 前面可以以任意数字结尾
                for k in range(n):  # 枚举前一步是哪个数
                    dp[i][j] += dp[k][j - nums[i]]
        
        # 所有以任意数字结尾的方案之和
        return sum(dp[i][target] for i in range(n))


# 70. 爬楼梯（进阶版）
topic="""
57. 爬楼梯（第八期模拟笔试）
题目描述
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 

每次你可以爬至多m (1 <= m < n)个台阶。你有多少种不同的方法可以爬到楼顶呢？ 

注意：给定 n 是一个正整数。

输入描述
输入共一行，包含两个正整数，分别表示n, m
输出描述
输出一个整数，表示爬到楼顶的方法数。
输入示例
3 2
输出示例
3
提示信息
数据范围：
1 <= m < n <= 32;

当 m = 2，n = 3 时，n = 3 这表示一共有三个台阶，m = 2 代表你每次可以爬一个台阶或者两个台阶。

此时你有三种方法可以爬到楼顶。


1 阶 + 1 阶 + 1 阶段
1 阶 + 2 阶
2 阶 + 1 阶
"""
import sys

def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    dp=[0]*(n+1)
    dp[0]=1
    for j in range(1,n+1):
        for i in range(1,m+1):
            if j>=i:
                dp[j]=dp[j]+dp[j-i]
    # print(dp)
    print(dp[n])







