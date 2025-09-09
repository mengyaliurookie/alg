# 0,1背包问题
# 二维dp数组的情况
# 思路就是选和不选当前物品，不选的话就是dp[i-1][j],选当前物品的话，那么就需要看看除去当前物品的重量的情况下不选当前物品的dp值加上当前物品的价值
# 两者取最大值
# 这中间因为要减去重量，所以需要加条件，就是只有背包容量大于的时候才能减，不然只能是不选当前物品，因为装不下


import sys

def main():
    m,n=sys.stdin.readline().strip().split()
    # print(f'm: {m}')
    # print(f'n: {n}')
    m,n=int(m),int(n)
    weights=sys.stdin.readline().strip().split()
    values=sys.stdin.readline().strip().split()
    # dp[m][n]表示1到m中商品在n的行李空间下，最优价值是多少
    # 递推公式是
    # 选m这个材料，和不选m这个材料
    # dp[m][n]=max(dp[m-1][n],values[m]+dp[m-1][n-weights[m]])
    # 初始化
    dp=[[0]*(n+1) for _ in range(m)]
    for i in range(n+1):
        if i>=int(weights[0]):
            dp[0][i]=int(values[0])
    # print(dp)
    for i in range(1,m):
        for j in range(1,n+1):
            # 从第二个商品开始抉择
            if j>=int(weights[i]):
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-int(weights[i])]+int(values[i]))
            else:
                dp[i][j]=dp[i-1][j]
    # print(dp)
    print(dp[m-1][n])

# if __name__=="__main__":
#     main()


# 滚动数组的情况
# 要注意在遍历背包的时候，要从打到小的去遍历，因为如果从小到大的话，会把当前物品重复加入背包
import sys

def main():
    m,n=sys.stdin.readline().strip().split()
    # print(f'm: {m}')
    # print(f'n: {n}')
    m,n=int(m),int(n)
    weights=sys.stdin.readline().strip().split()
    values=sys.stdin.readline().strip().split()
    # dp[m][n]表示1到m中商品在n的行李空间下，最优价值是多少
    # 递推公式是
    # 选m这个材料，和不选m这个材料
    # dp[m][n]=max(dp[m-1][n],values[m]+dp[m-1][n-weights[m]])
    # 初始化
    
    # 改成一维数组的情况
    dp=[0]*(n+1)
    for i in range(n+1):
        if i>=int(weights[0]):
            dp[i]=int(values[0])
    for i in range(1,m):
        for j in range(n,-1,-1):
            if j>=int(weights[i]):
                # 当背包容量大于当前物品重量的时候，才考虑要不要把当前物品加到背包中
                dp[j]=max(dp[j],dp[j-int(weights[i])]+int(values[i]))
            # else:
            #     # 否则就选择i-1件物品的最大值就是不变
            #     dp[j]=dp[]

    # print(dp)
    print(dp[n])

# if __name__=="__main__":
#     main()
    
# 416. 分割等和子集
topic="""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 可以转化为0,1背包问题，背包容量为sum(nums)/2
        s=sum(nums)
        if s%2==1:return False
        bag=int(s/2)
        # 从这些数字里面选能恰好装满bag的
        # 递推公式怎么写呢，肯定选能装下，并且是最大的
        n=len(nums)
        # print(f"bag:{bag}")
        dp=[0]*(bag+1)
        for i in range(bag+1):
            if i>=nums[0]:
                dp[i]=nums[0]
        for i in range(1,n):
            for j in range(bag,nums[i]-1,-1):
                 dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
        # print(dp)
        ans=None
        if dp[bag]==bag:
            ans=True
        else:
            ans=False
        return ans







