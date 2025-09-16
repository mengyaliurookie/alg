# 121. 买卖股票的最佳时机
topic="""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
# 记忆化搜索的方式
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 在每一天都需要做决策，如果当前以买入，则可以选择卖还是不卖
        # 如果当前还没有买入，则可以选择买还是不买
        # 买或者卖或者啥都不干，三种选择，最后看最大收益
        # dp=[0]*len(prices)
        n=len(prices)
        @cache
        def dfs(i,isb):
            if i==n:
                return 0
            # 如果之前没有买入过，
            left=0
            right=0
            if not isb:
                # 则可以选择买入
                l1=dfs(i+1,True)-prices[i]
                # 或者啥也不干
                l2=dfs(i+1,False)
                left=max(l1,l2)
            else:
                # 之前已经买入过，则可以选择啥也不干
                r1=dfs(i+1,True)
                # 或者直接卖出
                r2=prices[i]
                right=max(r1,r2)
            return max(left,right)
        return dfs(0,False)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 在每一天都需要做决策，如果当前以买入，则可以选择卖还是不卖
        # 如果当前还没有买入，则可以选择买还是不买
        # 买或者卖或者啥都不干，三种选择，最后看最大收益
        # 先用二维dp数组,
        # dp[i][j]表示在第i天的j状态下的最大利润，其中j=0表示持有股票最大利润，j=1表示不持有股票最大利润
        # 递推公式
        # 当前天持有股票，只能从上一天没持有股票，但是今天买入，和上一天跟来就持有股票，现在啥也不干推出
        # 当前天未持有股票，只能从上一天持有股票，但是今天卖出，和上一天未持有股票，现在啥也不干得出
        # dp[i][0]=max(dp[i-1][1]+prices[i],dp[i-1][1])
        n=len(prices)
        dp=[[0,0] for _ in range(n+1)]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,n):
            dp[i][0]=max(-prices[i],dp[i-1][0])
            dp[i][1]=max(dp[i-1][0]+prices[i],dp[i-1][1])
        return dp[n-1][1]
        # @cache
        # def dfs(i,isb):
        #     if i==n:
        #         return 0
        #     # 如果之前没有买入过，
        #     left=0
        #     right=0
        #     if not isb:
        #         # 则可以选择买入
        #         l1=dfs(i+1,True)-prices[i]
        #         # 或者啥也不干
        #         l2=dfs(i+1,False)
        #         left=max(l1,l2)
        #     else:
        #         # 之前已经买入过，则可以选择啥也不干
        #         r1=dfs(i+1,True)
        #         # 或者直接卖出
        #         r2=prices[i]
        #         right=max(r1,r2)
        #     return max(left,right)
        # return dfs(0,False)
            
# 122.买卖股票的最佳时机II
topic="""
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。

 

示例 1：

输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
最大总利润为 4 + 3 = 7 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
最大总利润为 4 。
示例 3：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0。
"""
# 贪心策略
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只要跌，当你持有股票的时候就会赔钱，所以要在跌之前卖出
        # 只要涨那就会赚钱，所以要在上涨之前购入股票，这样才会把所有收益获得，而避免所有损失
        ans=0
        n=len(prices)
        for i in range(1,n):
            tem=prices[i]-prices[i-1]
            if tem>0:
                ans+=tem
        return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只要跌，当你持有股票的时候就会赔钱，所以要在跌之前卖出
        # 只要涨那就会赚钱，所以要在上涨之前购入股票，这样才会把所有收益获得，而避免所有损失
        # 使用动态规划的方式
        # dp[i][j]表示第i天j状态下的最大利润
        # j=0：表示持有股票状态，j=1：表示未持有股票状态
        # 递推公式：
        # dp[i][0]=dp[i-1][1]-prices[i],dp[i-1][0]
        # dp[i][1]=dp[i-1][0]+prices[i],dp[i-1][1]
        dp=[[0,0] for _ in range(len(prices))]
        dp[0][0]=-prices[0]
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][1]-prices[i],dp[i-1][0])
            dp[i][1]=max(dp[i-1][0]+prices[i],dp[i-1][1])
        return dp[len(prices)-1][1]
        # ans=0
        # n=len(prices)
        # for i in range(1,n):
        #     tem=prices[i]-prices[i-1]
        #     if tem>0:
        #         ans+=tem
        # return ans
        
# 123.买卖股票的最佳时机III
topic="""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3：

输入：prices = [7,6,4,3,1] 
输出：0 
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
示例 4：

输入：prices = [1]
输出：0
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 当前抉择
        # 如果已经卖出过两次，那么之后啥也不干
        # 如果卖出过一次或者没有，那么需要看当前是持有股票，还是未持有，可以选择买入或者不买
        # 如果未进行过交易，也可以选则买入或者不买
        # dp[i][j][k] i表示第i天，j表示是否持有股票，k表示卖出次数，可以为0,1,2
        # 递推公式:j=0表示未持有股票,j=1表示持有股票
        # dp[i][0][0]=dp[i-1][0][0],
        # dp[i][0][1]=dp[i-1][0][1],dp[i-1][1][0]+prices[i]
        # dp[i][0][2]=dp[i-1][1][1]+prices[i],dp[i-1][0][2]
        # dp[i][1][0]=dp[i-1][0][0]-prices[i],dp[i-1][1][0]
        # dp[i][1][1]=dp[i-1][0][1]-prices[i],dp[i-1][1][1]
        n=len(prices)
        dp=[[[-math.inf,-math.inf,-math.inf],[-math.inf,-math.inf,-math.inf]] for _ in range(len(prices))]
        # 进行初始化
        dp[0][0][0] = 0
        dp[0][1][0]=-prices[0]
        for i in range(1,len(prices)):
            dp[i][0][0]=dp[i-1][0][0]
            dp[i][0][1]=max(dp[i-1][0][1],dp[i-1][1][0]+prices[i])
            dp[i][0][2]=max(dp[i-1][1][1]+prices[i],dp[i-1][0][2])
            dp[i][1][0]=max(dp[i-1][0][0]-prices[i],dp[i-1][1][0])
            dp[i][1][1]=max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])
        # print(dp)
        return max(
    dp[n-1][0][0],
    dp[n-1][0][1],
    dp[n-1][0][2]
)

        









