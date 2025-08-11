
# 242.有效的字母异位词

topic="""
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 通过字典来统计s中的字符分布，
        # 然后遍历t来减去字符，最后判断字典中是否全为0
        d=defaultdict(int)
        n=len(s)
        m=len(t)
        if n!=m:return False
        for i in range(n):
            d[s[i]]+=1
            d[t[i]]-=1
        ans=True
        for k in d.values():
            if k!=0:
                ans=False
                break
        return ans

# 349. 两个数组的交集

topic="""
    给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 感觉还是可以用字典计数的方式
        d=dict()
        for i in nums1:
            if i not in d:
                d[i]=1
        for j in nums2:
            if j in d:
                d[j]=0
        ans=[]
        for k,v in d.items():
            if v==0:
                ans.append(k)
        return ans

# 第202题. 快乐数

topic="""
    编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

 

示例 1：

输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # 无限循环的前提就是当前这个数已经在前面出现过了，此时就可以返回为false了
        # 否则就还有可能是快乐数
        # 所以需要一个哈希表来存储之前的数。
        def happy(n:int)->int:
            res=0
            while n:
                y=n%10 #余数
                res+=y*y
                n//=10 #
            return res
        s=set()
        ans=False
        while True:
            n=happy(n)
            if n==1:
                ans=True
                break
            if n in s:
                ans=False
                break
            s.add(n)
        # print(s)
        return ans

# 1. 两数之和
topic="""
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        ans=None
        for i,v in enumerate(nums):
            if target-v in d:
                ans=[i,d[target-v]]
                break
            else:
                d[v]=i

        return ans

