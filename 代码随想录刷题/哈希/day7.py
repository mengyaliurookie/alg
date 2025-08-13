
# 第454题.四数相加II

topic="""
    给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

示例 1：

输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

"""


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        d = defaultdict(int)
        for i in nums1:
            for j in nums2:
                d[i + j] += 1
        for l in nums4:
            for k in nums3:
                # print(d)
                if -(l + k) in d: ans += d[-(l + k)]
        return ans

# 383. 赎金信
topic="""
    给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

 

示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 统计一下两个字符串的分布，然后看看

        cnt = Counter()
        for i in magazine:
            cnt[i] += 1
        for j in ransomNote:
            cnt[j] -= 1
        ans = True
        for k, v in cnt.items():
            if v < 0:
                ans = False
                break
        return ans


# 第15题. 三数之和
topic="""
    给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 应该要排序一下，然后再去比较，不然不知道怎么移动
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            fn = nums[i]
            first = i + 1
            sec = len(nums) - 1
            # 去重第一个数
            if i > 0 and nums[i] == nums[i - 1]: continue
            # 遍历第二和第三个数
            while first < sec:
                r = fn + nums[first] + nums[sec]
                if r == 0:
                    res.append([fn, nums[first], nums[sec]])
                    # 去重第二个数
                    while first + 1 < len(nums) and nums[first] == nums[first + 1]:
                        first += 1
                    # 去重第三个数
                    while sec - 1 > first and nums[sec] == nums[sec - 1]:
                        sec -= 1
                    first += 1
                    sec -= 1
                elif r < 0:
                    first += 1
                else:
                    sec -= 1

        return list(res)

# 优化一些细节，比如剪枝处理
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 应该要排序一下，然后再去比较，不然不知道怎么移动
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n - 2):
            fn = nums[i]
            first = i + 1
            sec = len(nums) - 1
            # 优化，剪枝
            if fn + nums[first] + nums[i + 2] > 0:
                break
            if fn + nums[-2] + nums[-1] < 0:
                continue
            # 去重第一个数
            if i > 0 and nums[i] == nums[i - 1]: continue
            # 遍历第二和第三个数
            while first < sec:
                r = fn + nums[first] + nums[sec]
                if r == 0:
                    res.append([fn, nums[first], nums[sec]])
                    # 去重第二个数
                    while first + 1 < len(nums) and nums[first] == nums[first + 1]:
                        first += 1
                    # 去重第三个数
                    while sec - 1 > first and nums[sec] == nums[sec - 1]:
                        sec -= 1
                    first += 1
                    sec -= 1
                elif r < 0:
                    first += 1
                else:
                    sec -= 1

        return list(res)

# 第18题. 四数之和

topic="""
    给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 和三数之和类似的思路
        nums.sort()
        ans=[]
        n=len(nums)
        for f in range(n-3):
            fir=nums[f]
            # 跳过第一个重复的
            if f>0 and fir==nums[f-1]:continue
            for s in range(f+1,n-2):
                sec=nums[s]
                if s>f+1 and sec==nums[s-1]:continue
                thi=s+1
                fou=n-1
                while thi<fou:
                    r=fir+sec+nums[thi]+nums[fou]
                    if r==target:
                        ans.append([fir,sec,nums[thi],nums[fou]])
                        thi+=1
                        while thi<fou and nums[thi]==nums[thi-1]:
                            thi+=1
                        fou-=1
                        while fou>thi and nums[fou]==nums[fou+1]:
                            fou-=1
                    elif r<target:
                        thi+=1
                    else:
                        fou-=1
        return ans



