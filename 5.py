class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划二维dp
        # dp[i][j]表示i到j的字符串是不是回文子串
        # 当i处的字符等于j处的字符的时候，
        # 所以递推公式是if i==j:dp[i][j]=dp[i+1][j-1]
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # 初始化边界条件
        # 对角线上的元素都是1，因为此时i==j，只有一个元素，所以都是回文子串
        # 因为在判断的时候需要j-1，所以需要保证j大于等于1，所以需要把j=0的初始条件进行初始化
        for i in range(len(s)):
            dp[i][i] = 1
        # for i in range(len(s)):
        #     if s[i]==s[0]:
        #         dp[i][0]=1
        maxi = 0
        maxj = 0
        maxl = 0
        # 因为i，j依赖于i+1和j-1，所以遍历顺序i要反着来，不然当遍历到i的时候，i+1还没有确定
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i > 1:
                        # 大于等于3
                        dp[i][j] = 1 if dp[i + 1][j - 1] == 1 else 0
                        if dp[i][j] == 1:
                            if j - i + 1 > maxl:
                                maxi = i
                                maxj = j
                                maxl = j - i + 1
                    elif j - i == 1:
                        # 长度等于2
                        dp[i][j] = 1
                        if j - i + 1 > maxl:
                            maxi = i
                            maxj = j
                            maxl = j - i + 1

        return s[maxi:maxj + 1]
