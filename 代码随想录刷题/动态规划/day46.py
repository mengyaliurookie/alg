# 647. 回文子串
topic="""
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

 

示例 1：

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""
# 双指针的解法
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 新使用双指针的写法
        n=len(s)
        ans=0
        lastis=False
        for i in range(n):
            # 这种好像能获取到奇数个数的
            fir,sec=i,i
            # 指定双指针，然后向外扩散
            # 直到某个指针到达终点（即开头或者结尾）
            while not (fir==-1 or sec==n):
                if fir==sec:
                    # 只有一个字符
                    ans+=1
                    lastis=True
                elif sec-fir==1:
                    # 中间没有字符
                    if s[sec]==s[fir]:
                        ans+=1
                        lastis=True
                    else:
                        lastis=False
                else:
                    # 中间有字符
                    # 如果上一个是True
                    if s[sec]==s[fir]:
                        if lastis:
                            ans+=1
                    else:
                        lastis=False
                fir-=1
                sec+=1
        
        for j in range(1,n):
            # 这样可以来处理偶数的
            fir=j-1
            sec=j
            while not (fir==-1 or sec==n):
                if fir==sec:
                    # 只有一个字符
                    ans+=1
                    lastis=True
                elif sec-fir==1:
                    # 中间没有字符
                    if s[sec]==s[fir]:
                        ans+=1
                        lastis=True
                    else:
                        lastis=False
                else:
                    # 中间有字符
                    # 如果上一个是True
                    if s[sec]==s[fir]:
                        if lastis:
                            ans+=1
                    else:
                        lastis=False
                fir-=1
                sec+=1
        
        return ans


# 动态规划的形式
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 再使用动态规划的方式
        # dp[i][j]表示以i和j为边界的子区间字符串是不是回文子串
        # 递推公式是，当s[i]==s[j]的时候，需要判断i+1,j-1是不是回文子串，是的话那dp[i][j]也是
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        # 还需要初始化一下
        # 就是当i=n-1的时候和j=0的时候
        ans=0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if i==j:
                        dp[i][j]=True
                        ans+=1
                    elif j-i==1:
                        dp[i][j]=True
                        ans+=1
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j]=True
                            ans+=1
        return ans


# 516.最长回文子序列
topic="""
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
"""











