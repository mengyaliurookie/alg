# 300.最长递增子序列
topic="""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
"""
# 下面是会超时的递归，但是加了缓存之后结果就不正确了
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 先用递归和缓存的方式来
        # 数组中的元素添加到数组中与否
        n=len(nums)
        ans=0
        path=[]
        # @cache
        def dfs(i):
            # print(path)
            if i==n:
                nonlocal ans
                ans=max(len(path),ans)
                return 
            # 如果path是空的或者path中的最后一个元素小于nums[i]，那么就添加到path中
            # 最后要弹出，然后进入下一个递归
            if len(path)==0 or path[-1]<nums[i]:
                path.append(nums[i])
                dfs(i+1)
                path.pop()
            dfs(i+1)
        dfs(0)
        return ans

# 下面是动态规划的方式求解，通过了，但是时间复杂度是n平方的
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 先用递归和缓存的方式来
        # 数组中的元素添加到数组中与否
        n=len(nums)
        dp=[0]*n
        dp[0]=1
        for i in range(1,n):
            maxv=1
            for j in range(i):
                if nums[i]>nums[j]:
                    maxv=max(dp[j]+1,maxv)
            dp[i]=maxv
        # print(dp)
        return max(dp)

# 674. 最长连续递增序列
topic="""
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

 

示例 1：

输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。 
示例 2：

输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 用动态规划的方式求解
        # dp[i]表示以nums[i]结尾的元素的最长连续递增子序列的长度
        n=len(nums)
        dp=[1]*n
        # dp[0]=1
        ans=1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
            # else:
            #     dp[i]=1
            ans=max(ans,dp[i])
        return ans

# 718. 最长重复子数组
topic="""
给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。

 

示例 1：

输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。
示例 2：

输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 子数组是什么意思呢，需要连续
        # 怎么找公共子数组呢
        # dp[i][j],i，j分别表示以nums1[i]和nums2[j]结尾的子数组中公共的最长子数组的长度
        # 递推公式是：
        # dp[i][j]=if nums1[i]==nums2[j]:dp[i][j]=dp[i-1][j-1]+1
        n1=len(nums1)
        n2=len(nums2)
        dp=[[0]*n2 for _ in range(n1)]
        ans=0
        for i in range(n1):
            if nums1[i]==nums2[0]:
                dp[i][0]=1
                ans=1
        for j in range(n2):
            if nums2[j]==nums1[0]:
                dp[0][j]=1
                ans=1
        # print(dp)
        for i in range(1,n1):
            for j in range(1,n2):
                if nums1[i]==nums2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                ans=max(ans,dp[i][j])
        return ans
