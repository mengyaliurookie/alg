
# 3186 施咒的最大总伤害
topic="""
一个魔法师有许多不同的咒语。

给你一个数组 power ，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。

已知魔法师使用伤害值为 power[i] 的咒语时，他们就 不能 使用伤害为 power[i] - 2 ，power[i] - 1 ，power[i] + 1 或者 power[i] + 2 的咒语。

每个咒语最多只能被使用 一次 。

请你返回这个魔法师可以达到的伤害值之和的 最大值 。

 

示例 1：

输入：power = [1,1,3,4]

输出：6

解释：

可以使用咒语 0，1，3，伤害值分别为 1，1，4，总伤害值为 6 。

示例 2：

输入：power = [7,1,6,6]

输出：13

解释：

可以使用咒语 1，2，3，伤害值分别为 1，6，6，总伤害值为 13 。

 

提示：

1 <= power.length <= 105
1 <= power[i] <= 109
"""

# 深度优先搜索加缓存
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        dic={}
        for i in power:
            if i in dic:
                dic[i]+=i
            else:
                dic[i]=i
        # print(f"dic: {dic}")
        nums=list(dic.keys())
        nums.sort()
        # print(f"nums: {nums}")
        # 类似于上一道题，只不过是跳过的多一点
        # 选当前元素，不选当前元素
        # dp数组表示当前长度的数组，可以达到的伤害值之和的最大值
        # dp[n]=dp[n-1](不选当前元素)
        # 选当前元素：
        n=len(nums)
        @cache
        def dfs(i):
            if i>=n:
                return 0
            # 不选当前元素
            res=dfs(i+1)
            # 选当前
            j=i+1
            k=i+2
            # 当还存在下下个元素的时候，并且下一个元素等于nums[i]+1并且下下个元素等于nums[i]+2的时候
            if k<n and nums[j]==nums[i]+1 and nums[k]==nums[i]+2:
                res=max(dic[nums[i]]+dfs(i+3),res)
            # 当还存在下下个元素的时候，并且下一个元素等于nums[i]+1且下下个元素不等于nums[i]+2的时候
            elif (k<n and (nums[j]==nums[i]+1 and nums[k]!=nums[i]+2)):
                res=max(dic[nums[i]]+dfs(i+2),res)
            # 当存在下一个元素，并且下一个元素等于nums[i]+2或者等于nums[i]+1的时候
            elif (j<n and  (nums[j]==nums[i]+2 or nums[j]==nums[i]+1)):
                res=max(dic[nums[i]]+dfs(i+2),res)
            #
            else:
                res=max(dic[nums[i]]+dfs(i+1),res)
            return res
        return dfs(0)


# 动态规划版本
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        dic={}
        for i in power:
            if i in dic:
                dic[i]+=i
            else:
                dic[i]=i
        # print(f"dic: {dic}")
        nums=list(dic.keys())
        nums.sort()
        # print(f"nums: {nums}")
        # 类似于上一道题，只不过是跳过的多一点
        # 选当前元素，不选当前元素
        # dp数组表示当前长度的数组，可以达到的伤害值之和的最大值
        # dp[n]=dp[n-1](不选当前元素)
        # 选当前元素：
        n=len(nums)
        # 修改为动态规划的形式
        dp=[0]*(n)
        dp[0]=dic[nums[0]]
        if n==1:
            return dp[-1]
        dp[1]=max(dic[nums[0]],dic[nums[1]]) if abs(nums[0]-nums[1])==1 or abs(nums[0]-nums[1])==2 else dic[nums[0]]+dic[nums[1]]
        if n==2:
            return dp[-1]
        for i in range(2,n):
            # 不选当前
            res=dp[i-1]
            cur=dic[nums[i]]
            if nums[i]>nums[i-1]+2:
                # 此时都可以选
                res=max(res,dp[i-1]+cur)
            else:
                if nums[i]==nums[i-1]+2:
                    # 此时意味着i-2是可以选的
                    res=max(res,dp[i-2]+cur)
                else:
                    if nums[i]==nums[i-2]+2:
                        res=max(res,(dp[i-3] if i>2 else 0)+cur)
                    else:
                        res=max(res,dp[i-2]+cur)
            dp[i]=res
            # 选当前,可以选当前的话，必须是
            # 此时不能选i-1但是能选i-2
            # if nums[i]==nums[i-1]+2 or (nums[i]==nums[i-1]+1 and nums[i]!=nums[i-2]+2):
            #     res=max(dp[i-2]+dic[nums[i]],res)
            # # 此时不能选i-1也不能选i-2，需要判断是不是可以选i-3
            # elif nums[i]==nums[i-1]+1 and nums[i]==nums[i-2]+2:
            #     res=max(dp[i-3] if i>2 else 0+dic[nums[i]],res)
            # else:
            #     # 此时没有限制
            #     res=max(dp[i-1]+dic[nums[i]],res)
            dp[i]=res
        return dp[-1]


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        dic = {}
        for i in power:
            if i in dic:
                dic[i] += i
            else:
                dic[i] = i
        # print(f"dic: {dic}")
        nums = list(dic.keys())
        nums.sort()
        # print(f"nums: {nums}")
        # 类似于上一道题，只不过是跳过的多一点
        # 选当前元素，不选当前元素
        # dp数组表示当前长度的数组，可以达到的伤害值之和的最大值
        # dp[n]=dp[n-1](不选当前元素)
        # 选当前元素：
        n = len(nums)
        # 修改为动态规划的形式
        dp = [0] * (n)
        dp[0] = dic[nums[0]]
        if n == 1:
            return dp[-1]
        dp[1] = max(dic[nums[0]], dic[nums[1]]) if abs(nums[0] - nums[1]) == 1 or abs(nums[0] - nums[1]) == 2 else dic[
                                                                                                                       nums[
                                                                                                                           0]] + \
                                                                                                                   dic[
                                                                                                                       nums[
                                                                                                                           1]]
        if n == 2:
            return dp[-1]
        for i in range(2, n):
            # 不选当前
            res = dp[i - 1]
            # cur=dic[nums[i]]
            # if nums[i]>nums[i-1]+2:
            #     # 此时都可以选
            #     res=max(res,dp[i-1]+cur)
            # else:
            #     if nums[i]==nums[i-1]+2:
            #         # 此时意味着i-2是可以选的
            #         res=max(res,dp[i-2]+cur)
            #     else:
            #         if nums[i]==nums[i-2]+2:
            #             res=max(res,(dp[i-3] if i>2 else 0)+cur)
            #         else:
            #             res=max(res,dp[i-2]+cur)
            # dp[i]=res
            # 选当前,可以选当前的话，必须是
            # 此时不能选i-1但是能选i-2
            if nums[i] == nums[i - 1] + 2 or (nums[i] == nums[i - 1] + 1 and nums[i] != nums[i - 2] + 2):
                res = max(dp[i - 2] + dic[nums[i]], res)
            # 此时不能选i-1也不能选i-2，需要判断是不是可以选i-3
            elif nums[i] == nums[i - 1] + 1 and nums[i] == nums[i - 2] + 2:
                res = max((dp[i - 3] if i > 2 else 0) + dic[nums[i]], res)
            else:
                # 此时没有限制
                res = max(dp[i - 1] + dic[nums[i]], res)
            dp[i] = res
        return dp[-1]
