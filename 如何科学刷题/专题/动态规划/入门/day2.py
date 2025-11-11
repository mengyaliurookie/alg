
# 2466 统计构造好字符串的方案数
topic="""
给你整数 zero ，one ，low 和 high ，我们从空字符串开始构造一个字符串，每一步执行下面操作中的一种：

将 '0' 在字符串末尾添加 zero  次。
将 '1' 在字符串末尾添加 one 次。
以上操作可以执行任意次。

如果通过以上过程得到一个 长度 在 low 和 high 之间（包含上下边界）的字符串，那么这个字符串我们称为 好 字符串。

请你返回满足以上要求的 不同 好字符串数目。由于答案可能很大，请将结果对 109 + 7 取余 后返回。

 

示例 1：

输入：low = 3, high = 3, zero = 1, one = 1
输出：8
解释：
一个可能的好字符串是 "011" 。
可以这样构造得到："" -> "0" -> "01" -> "011" 。
从 "000" 到 "111" 之间所有的二进制字符串都是好字符串。
示例 2：

输入：low = 2, high = 3, zero = 1, one = 2
输出：5
解释：好字符串为 "00" ，"11" ，"000" ，"110" 和 "011" 。
 

提示：

1 <= low <= high <= 105
1 <= zero, one <= low
 

"""
# 记忆化搜索的方式
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans = 0

        @cache
        def dfs(n):
            if n > high:
                return 0

            res = 1 if n >= low and n <= high else 0

            res += dfs(n + zero)
            res += dfs(n + one)
            # 总共有两种情况，加zero个0，加one个1
            return res % 1000000007

        # dfs(0)
        return dfs(0)

# 转化为动态规划的形式
class Solution:
    def countGoodStrings(self, low, high, zero, one):
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1  # 对应 dfs(0) 的初始状态

        for n in range(1, high + 1):
            # 对应 dfs(n) 依赖 dfs(n-zero) 和 dfs(n-one)
            if n >= zero:
                dp[n] += dp[n - zero]
            if n >= one:
                dp[n] += dp[n - one]
            dp[n] %= MOD

        # 对应 dfs(0) 累加 [low, high] 范围内的结果
        return sum(dp[low:high + 1]) % MOD

# 2266 统计打字方案数
topic="""
Alice 在给 Bob 用手机打字。数字到字母的 对应 如下图所示。



为了 打出 一个字母，Alice 需要 按 对应字母 i 次，i 是该字母在这个按键上所处的位置。

比方说，为了按出字母 's' ，Alice 需要按 '7' 四次。类似的， Alice 需要按 '5' 两次得到字母  'k' 。
注意，数字 '0' 和 '1' 不映射到任何字母，所以 Alice 不 使用它们。
但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息 。

比方说，Alice 发出的信息为 "bob" ，Bob 将收到字符串 "2266622" 。
给你一个字符串 pressedKeys ，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息 。

由于答案可能很大，将它对 109 + 7 取余 后返回。

 

示例 1：

输入：pressedKeys = "22233"
输出：8
解释：
Alice 可能发出的文字信息包括：
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
由于总共有 8 种可能的信息，所以我们返回 8 。
示例 2：

输入：pressedKeys = "222222222222222222222222222222222222"
输出：82876089
解释：
总共有 2082876103 种 Alice 可能发出的文字信息。
由于我们需要将答案对 109 + 7 取余，所以我们返回 2082876103 % (109 + 7) = 82876089 。
 

提示：

1 <= pressedKeys.length <= 105
pressedKeys 只包含数字 '2' 到 '9' 。
"""

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        # 当选1个2然后转化为子问题
        # 当选2个2然后转化为子问题
        # 当选3个2然后转化为子问题
        # 当选到最后没得选了，就返回1，
        dic = {'2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 4, '8': 3, '9': 4}
        l = len(pressedKeys)
        # dfs用来求相同的字母可以组合成的字符种类
        # f(4)=f(3)+f(2)+f(1)+f(0)
        # 或者f(4)=f(3)+f(2)+f(1)
        start = 0
        ans = 1
        while start < l:
            end = start + 1
            while end < l and pressedKeys[start] == pressedKeys[end]:
                end += 1
            ans *= self.getsame(end - start, dic[pressedKeys[start]])
            ans %= 1000000007
            start = end
        return ans

    def getsame(self, n, ty):
        if n >= 4:
            dp = [0] * (n + 1)
        else:
            dp = [0] * 4
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n + 1):
            if ty == 3:
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            else:
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]
        return dp[n] % 1000000007

