
# 122.买卖股票的最佳时机 II
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
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只要跌，当你持有股票的时候就会赔钱，所以要在跌之前卖出
        # 只要涨那就会赚钱，所以要在上涨之前购入股票，这样才会把所有收益获得，而避免所有损失
        ans = 0
        n = len(prices)
        for i in range(1, n):
            tem = prices[i] - prices[i - 1]
            if tem > 0:
                ans += tem
        return ans

# 55. 跳跃游戏
topic="""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 可以到达最后一个位置，就是找到当前坐标可以到达的区域内的坐标可以到达的最远距离如果
        maxlength=nums[0]
        n=len(nums)
        ind=0
        while ind<=maxlength and ind<n:
            maxlength=max(maxlength,nums[ind]+ind)
            ind+=1
            if maxlength>=n-1:break
        ans=None
        if maxlength>=len(nums)-1:
            ans=True
        else:
            ans=False
        return ans


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 可以到达最后一个位置，就是找到当前坐标可以到达的区域内的坐标可以到达的最远距离如果
        max_depth = 0

        for index, item in enumerate(nums):
            if index > max_depth:
                return False
            if index + item > max_depth:
                max_depth = index + item

        return True

# 45.跳跃游戏 II
topic="""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：

0 <= j <= nums[i] 且
i + j < n
返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。

 

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
"""

# 可以转化为子问题的形式，即，直接选择可以跳到最后位置的里面挑一个，然后在里面接着找
# 可以到达最后一个位置，那么一定可以到达任何一个位置
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        n = len(nums)
        max_depth = 0
        cur_start = 0
        for i in range(n - 1):
            max_depth = max(max_depth, i + nums[i])
            if i == cur_start:
                step += 1
                cur_start = max_depth
        return step



# 1005.K次取反后最大化的数组和
topic="""
    给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：

选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
重复这个过程恰好 k 次。可以多次选择同一个下标 i 。

以这种方式修改数组后，返回数组 可能的最大和 。

 

示例 1：

输入：nums = [4,2,3], k = 1
输出：5
解释：选择下标 1 ，nums 变为 [4,-2,3] 。
示例 2：

输入：nums = [3,-1,0,2], k = 3
输出：6
解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
示例 3：

输入：nums = [2,-3,-1,5,-4], k = 2
输出：13
解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
"""
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 需要排序，先把所有负数都取反
        # 如果剩下都是正数了，并且剩下的k是偶数，那就结束，如果是奇数，那就把最小的变为负数
        nums.sort()
        ind=0
        n=len(nums)
        while k>0 and ind<n:
            if nums[ind]<0:
                nums[ind]=-nums[ind]
            elif nums[ind]==0:
                break
            else:
                # 此时所有都大于零，并且ind指向的是第一个大于零数，并且上一个一定是小于零数
                if k%2==0:
                    break
                else:
                    if ind>0:
                        if nums[ind-1]>nums[ind]:
                            nums[ind]=-nums[ind]
                        else:
                            nums[ind-1]=-nums[ind-1]
                    else:
                        nums[ind]=-nums[ind]
                    break
            ind+=1
            k-=1
        if ind==n:
            if k%2!=0:
                nums[ind-1]=-nums[ind-1]
        ans=0
        for i in nums:
            ans+=i
        return ans

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()  # 从小到大排序

        for i, x in enumerate(nums):  # 优先改最小的
            if k == 0 or x >= 0:  # 修改次数用尽，或者负数已全部取反
                break
            nums[i] *= -1  # 负数取反
            k -= 1  # 消耗一次修改次数

        # 如果剩余的 k 是奇数，选最小的数取反
        return sum(nums) - (min(nums) * 2 if k % 2 else 0)





