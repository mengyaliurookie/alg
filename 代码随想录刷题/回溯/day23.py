
# 491.递增子序列
topic="""
    给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。

数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

 

示例 1：

输入：nums = [4,6,7,7]
输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
示例 2：

输入：nums = [4,4,3,2,1]
输出：[[4,4]]
 

提示：

1 <= nums.length <= 15
-100 <= nums[i] <= 100
"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 加入到path中的时候，需要判断当前元素是不是大于path末尾元素
        # 而要可以从每个位置开始出发到最后，而且只要大于2就要添加到ans中
        # 因为元素有重复还需要去重，但是去重的逻辑不是按照排序的那么来，
        ans = []
        path = []
        n = len(nums)

        def dfs(start):
            if len(path) >= 2:
                ans.append(path[:])
            used = set()  # 记录当前层已经使用过的元素
            for i in range(start, n):
                if nums[i] in used:
                    continue
                if len(path) == 0 or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    dfs(i + 1)
                    path.pop()
                # else:
                #     path.append(nums[i])
                #     dfs(i+1)
                #     path.pop()

        dfs(0)
        # print(ans)
        return ans

# 46.全排列
topic="""
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 全排列的话，就是选完这个还可以选
        # 但是需要在深度上面记录选过的不能再选了
        # 组合是可以通过控制层数开始的位置来过滤和去重
        n=len(nums)
        ans=[]
        path=[]
        used=[False]*n
        def dfs(d):
            if d==n:
                ans.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    path.append(nums[i])
                    used[i]=True
                    dfs(d+1)
                    used[i]=False
                    path.pop()
        dfs(0)
        return ans

# 47.全排列 II
topic="""
    给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 相比元素不重复的全排列，还需要加一个每一层的去重，
        n = len(nums)
        used = [False] * n
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path[:])
                return
            layer = set()
            for j in range(n):
                if not used[j]:
                    # print(f'第{i}层：',layer)
                    if nums[j] in layer:
                        continue
                    layer.add(nums[j])
                    used[j] = True
                    path.append(nums[j])
                    dfs(i + 1)
                    path.pop()
                    used[j] = False

        dfs(0)
        return ans


















