
# 740 删除并获得点数
topic="""
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

 

示例 1：

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
示例 2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
 

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 转化为子问题的话，就是随便删除一个，然后执行删除x-1,x+1，
        # 然后就是子问题了，接着删除一个
        # 但是问题是怎么来表示删除操作能够时间复杂度低一点。
        nums.sort()
        # 先分组求和一下，然后
        dic = {}
        s = []
        for i in nums:
            if i not in dic:
                dic[i] = i
                s.append(i)
            else:
                dic[i] += i
        # 子问题的话，就是，删除当前节点，和不删除当前节点，
        n = len(s)
        ans = 0

        @cache
        def dfs(i):
            if i >= n:
                # nonlocal ans
                # ans=max(ans,su)
                return 0
            # 挑选当前节点
            left = 0
            j = i + 1
            if j < n and s[j] == s[i] + 1:
                left = dfs(i + 2) + dic[s[i]]
            else:
                left = dfs(j) + dic[s[i]]

            # 不挑选当前节点
            right = dfs(i + 1)
            return max(left, right)

        return dfs(0)

# 动态规划的形式
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 转化为子问题的话，就是随便删除一个，然后执行删除x-1,x+1，
        # 然后就是子问题了，接着删除一个
        # 但是问题是怎么来表示删除操作能够时间复杂度低一点。
        nums.sort()
        # 先分组求和一下，然后
        dic={}
        s=[]
        for i in nums:
            if i not in dic:
                dic[i]=i
                s.append(i)
            else:
                dic[i]+=i
        # 子问题的话，就是，删除当前节点，和不删除当前节点，
        n=len(s)
        dp=[0]*(n)
        dp[0]=dic[s[0]]
        for i in range(1,n):
            left=dp[i-1]
            if s[i]-1==s[i-1]:
                right=(dp[i-2] if i>1 else 0)+dic[s[i]]
            else:
                right=dp[i-1]+dic[s[i]]
            dp[i]=max(left,right)
        return dp[-1]