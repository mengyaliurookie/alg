
# 198.打家劫舍
topic="""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 有两个子问题，当偷这个的时候，那么下一家就不能偷了，当不偷这一家的时候，下一家是可以偷的
        n=len(nums)
        @cache
        def dfs(i):
            if i>=n:
                return 0
            # 偷
            left=dfs(i+2)+nums[i]
            right=dfs(i+1)
            return max(left,right)
        return dfs(0)

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 有两个子问题，当偷这个的时候，那么下一家就不能偷了，当不偷这一家的时候，下一家是可以偷的
        n=len(nums)
        dp=[0]*(n+1)
        dp[1]=nums[0]
        for i in range(1,n+1):
            # print(i)
            if i>=2:
                dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[n]
        # @cache
        # def dfs(i):
        #     if i>=n:
        #         return 0
        #     # 偷
        #     left=dfs(i+2)+nums[i]
        #     right=dfs(i+1)
        #     return max(left,right)
        # return dfs(0)


# 213.打家劫舍II
topic="""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

 

示例 1：

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：

输入：nums = [1,2,3]
输出：3
"""
# 记忆化搜搜的方式
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 需要分情况来讨论，偷第一个，就只能到n-1
        # 不偷第一个，就可以到n
        n=len(nums)
        if n==1:
            return nums[0]
        @cache
        def dfs(i):
            if i>=n:
                return 0
            # 偷这个
            left=dfs(i+2)+nums[i]
            right=dfs(i+1)
            return max(left,right)
        @cache
        def dfs1(i):
            if i>=n-1:
                return 0
            left=dfs1(i+2)+nums[i]
            right=dfs1(i+1)
            return max(left,right)
        ans1=dfs(1)
        ans2=dfs1(0)
        return max(ans1,ans2)

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 需要分情况来讨论，偷第一个，就只能到n-1
        # 不偷第一个，就可以到n
        # 改成动态规划的形式
        # fir=nums[]
        if len(nums)==1:return nums[0]
        return max(self.dpte(nums[1:]),self.dpte(nums[:-1]))
        # if n==1:
        #     return nums[0]   
        # @cache
        # def dfs(i):
        #     if i>=n:
        #         return 0
        #     # 偷这个
        #     left=dfs(i+2)+nums[i]
        #     right=dfs(i+1)
        #     return max(left,right)
        # @cache
        # def dfs1(i):
        #     if i>=n-1:
        #         return 0
        #     left=dfs1(i+2)+nums[i]
        #     right=dfs1(i+1)
        #     return max(left,right)
        # ans1=dfs(1)
        # ans2=dfs1(0)
        # return max(ans1,ans2)
    def dpte(self,nums):
        n=len(nums)
        dp=[0]*(n+1)
        dp[1]=nums[0]
        for i in range(1,n+1):
            # print(i)
            if i>=2:
                dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[n]


# 337.打家劫舍 III
topic="""
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

 

示例 1:



输入: root = [3,2,3,null,3,null,1]
输出: 7 
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
示例 2:



输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 不偷当前节点，则左子树和右子树成为子问题
        # 偷当前节点，则左子树，右子树的头结点都不能偷，可能会转化为四个子问题
        @cache
        def dfs(root):
            if root is None:
                return 0
            nch=dfs(root.left)+dfs(root.right)
            ch=root.val
            if root.left:
                ch+=dfs(root.left.left)
                ch+=dfs(root.left.right)
            if root.right:
                ch+=dfs(root.right.left)
                ch+=dfs(root.right.right)
            return max(nch,ch)
        return dfs(root)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 不偷当前节点，则左子树和右子树成为子问题
        # 偷当前节点，则左子树，右子树的头结点都不能偷，可能会转化为四个子问题
        # 树形dp，dp是一个两个变量的数组，0表示选当前节点，1表示不选当前节点
        # 转化为dp
        def dfs(root):
            if root is None:
                return (0,0)
            left=dfs(root.left)
            right=dfs(root.right)
            val0=left[1]+right[1]+root.val
            # 不选当前节点的话，那么选左节点不选右节点，左右节点都不选，选右节点不选左节点
            # 左右都不选的情况包含在了选一个中
            val1=max(left[1],left[0])+max(right[0],right[1])
            return (val0,val1)
        return max(dfs(root))

        




