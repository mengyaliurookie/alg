# 188.买卖股票的最佳时机IV
topic="""
给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 和那个第三个题很类似，
        n=len(prices)
        dp=[[[-math.inf]*(k+1),[-math.inf]*(k+1)] for _ in range(len(prices))]
        # 进行初始化
        dp[0][0][0] = 0
        dp[0][1][0]=-prices[0]
        for i in range(1,len(prices)):
            dp[i][0][0]=dp[i-1][0][0]
            for j in range(1,k+1):
                dp[i][0][j]=max(dp[i-1][0][j],dp[i-1][1][j-1]+prices[i])
            for j in range(k):
                dp[i][1][j]=max(dp[i-1][0][j]-prices[i],dp[i-1][1][j])
        return max(dp[n-1][0])
        

# 309.最佳买卖股票时机含冷冻期
topic="""
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
示例 2:

输入: prices = [1]
输出: 0
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][j][k]表示第i天的j状态下的最大利润
        # j=0表示未持有股票，j=1表示持有股票
        # k=0表示未处于冷冻期，k=1表示处于冷冻期
        # dp[i][0][0]=dp[i-1][0][0],dp[i-1][0][1] 
        # dp[i][0][1]=dp[i-1][1][0]+prices[i-1]
        # dp[i][1][0]=dp[i-1][0][0]-prices[i-1],dp[i-1][1][0]
        #
        n=len(prices)
        dp=[[[-math.inf,-math.inf],[-math.inf,-math.inf]] for _ in range(n+1)]
        dp[0][1][0]=-prices[0]
        dp[0][0][0]=0
        for i in range(1,n):
            dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1])  # 不持股，不冷冻
            dp[i][0][1] = dp[i-1][1][0] + prices[i]          # 今天卖出 -> 进入冷冻期
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])  
        return max(dp[n-1][0])

# 714.买卖股票的最佳时机含手续费
topic="""
给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

 

示例 1：

输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
示例 2：

输入：prices = [1,3,7,5,10,3], fee = 3
输出：6
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 可以只在卖出的时候支付手续费
        # dp[i][j]表示第i天状态j下的最大收益
        # 递推公式是
        # j=0表示未持有股票，j=1表示持有股票
        # dp[i][0]=dp[i-1][1]+prices[i]-fee,dp[i-1][0]
        # dp[i][1]=dp[i-1][0]-prisex[i],dp[i-1][1]
        n=len(prices)
        dp=[[-math.inf,-math.inf] for _ in range(n)]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][1]+prices[i]-fee,dp[i-1][0])
            dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][1])
        return dp[n-1][0]


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 可以只在卖出的时候支付手续费
        # dp[i][j]表示第i天状态j下的最大收益
        # 递推公式是
        # j=0表示未持有股票，j=1表示持有股票
        # dp[i][0]=dp[i-1][1]+prices[i]-fee,dp[i-1][0]
        # dp[i][1]=dp[i-1][0]-prisex[i],dp[i-1][1]
        n=len(prices)
        # 尝试优化一下空间
        a=0
        b=-prices[0]
        for i in range(1,n):
            a,b=max(b+prices[i]-fee,a),max(a-prices[i],b)
        return a
        # dp=[[-math.inf,-math.inf] for _ in range(n)]
        # dp[0][0]=0
        # dp[0][1]=-prices[0]
        # for i in range(1,n):
        #     dp[i][0]=max(dp[i-1][1]+prices[i]-fee,dp[i-1][0])
        #     dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][1])
        # return dp[n-1][0]


