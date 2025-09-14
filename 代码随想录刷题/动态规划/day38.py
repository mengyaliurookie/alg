
# 322. 零钱兑换
topic="""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
 
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 先用记忆化搜索的方式来处理一下
        # 子问题是，当选择某一枚硬币的时候，和不选某一枚硬币的时候
        n=len(coins)
        @cache
        def dfs(i,c):
            if i<0:
                return 0 if c==0 else inf
            if c<coins[i]:#只能不选
                return dfs(i-1,c)
            return min(dfs(i-1,c),dfs(i,c-coins[i])+1)
        ans=dfs(n-1,amount)
        return ans if ans<inf else -1

# 279.完全平方数
topic="""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

 

示例 1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
 
提示：

1 <= n <= 104
"""
@cache
def dfs(n,i):
    if i==0:
        return inf if n else 0
    if i*i>n:
        return dfs(n,i-1)
    return min(dfs(n,i-1),dfs(n-i*i,i)+1)

class Solution:
    def numSquares(self, n: int) -> int:
        
        return dfs(n,isqrt(n))
        

# 139.单词拆分
topic="""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""







