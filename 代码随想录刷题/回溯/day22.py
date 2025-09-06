
# 131.分割回文串
topic="""
    给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 转化为子问题的话，就是当前面几个是回文串的时候，递归剩下的字符串，否则不递归
        # 这样，可以确定到达字符串末尾的时候，前面的一定都是回文串，此时就可以加入结果集
        ans = []
        path = []
        n = len(s)

        def ishw(s: str) -> bool:
            n = len(s)
            fir = 0
            sec = n - 1
            ans = True
            while fir < sec:
                if s[fir] != s[sec]:
                    ans = False
                    break
                else:
                    fir += 1
                    sec -= 1
            return ans

        def dfs(ind):
            if ind == n:
                ans.append(path.copy())
                return
            for i in range(ind, n):
                if ishw(s[ind:i + 1]):
                    path.append(s[ind:i + 1])
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return ans

# 另一种方式，选或不选
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 转化为子问题的话，就是当前面几个是回文串的时候，递归剩下的字符串，否则不递归
        # 这样，可以确定到达字符串末尾的时候，前面的一定都是回文串，此时就可以加入结果集
        ans = []
        path = []
        n = len(s)

        # 选或不选的方法
        # 需要记录不选的时候字符的开始位置
        def dfs(ind, start):
            if ind == n:
                ans.append(path.copy())
                return

            # 不分割，不选i
            if ind < n - 1:  # i=n-1时只能分割
                dfs(ind + 1, start)
            # 分割，需要判断start到i+1直接的子字符是不是回文，是的话才需要递归
            t = s[start:ind + 1]
            if t == t[::-1]:
                path.append(t)
                dfs(ind + 1, ind + 1)
                path.pop()

        dfs(0, 0)
        return ans


# 93.复原IP地址
topic="""
    有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

 

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 可以转化为子问题的形式
        # 当选定某一个符合规则的整数之后，剩下的字符串就是一个子问题
        # 所以会用到字符串开始的位置，start，以及ip地址的剩下还有几个，k
        # 中间截取的过程中，如果当前是0，那么必须作为一个整数来处理
        # 如果不是，那么要穷举完在0-255之间满足范围的各个字符片段
        ans = []
        path = []
        n = len(s)

        def dfs(start, k):
            if k == 0 and start == n:
                ans.append(".".join(path))
                return
            if start >= n: return
            if k <= 0: return
            # 现在需要判断以start开头的前几个字符是不是满足要求了
            if s[start] == '0':
                # 直接进入下一个递归
                path.append(s[start])
                dfs(start + 1, k - 1)
                path.pop()
            else:
                end = n if start + 3 >= n else start + 3
                for ind in range(start, end):
                    intnum = int(s[start:ind + 1])
                    if intnum > 0 and intnum <= 255:
                        path.append(s[start:ind + 1])
                        dfs(ind + 1, k - 1)
                        path.pop()

        dfs(0, 4)
        return ans

# 剪枝
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 可以转化为子问题的形式
        # 当选定某一个符合规则的整数之后，剩下的字符串就是一个子问题
        # 所以会用到字符串开始的位置，start，以及ip地址的剩下还有几个，k
        # 中间截取的过程中，如果当前是0，那么必须作为一个整数来处理
        # 如果不是，那么要穷举完在0-255之间满足范围的各个字符片段
        ans = []
        path = []
        n = len(s)

        def dfs(start, k):
            if n - start < k: return
            if k == 0 and start == n:
                ans.append(".".join(path))
                return
            if start >= n: return
            if k <= 0: return
            # 现在需要判断以start开头的前几个字符是不是满足要求了
            if s[start] == '0':
                # 直接进入下一个递归
                path.append(s[start])
                dfs(start + 1, k - 1)
                path.pop()
            else:
                end = n if start + 3 >= n else start + 3
                for ind in range(start, end):
                    intnum = int(s[start:ind + 1])
                    if intnum > 0 and intnum <= 255:
                        path.append(s[start:ind + 1])
                        dfs(ind + 1, k - 1)
                        path.pop()

        dfs(0, 4)
        return ans


# 78.子集
topic="""
    给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 这需要再加一个递归，就是不选当前元素的情况
        n = len(nums)
        ans = []
        path = []

        def dfs(ind):
            if ind == n:
                ans.append(path[:])
                return
            # 不选当前元素
            dfs(ind + 1)
            # 选当前元素
            path.append(nums[ind])
            dfs(ind + 1)
            path.pop()

        dfs(0)
        return ans

# 方法二：
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 这需要再加一个递归，就是不选当前元素的情况
        n = len(nums)
        ans = []
        path = []

        def dfs(ind):
            ans.append(path[:])
            for j in range(ind, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return ans

# 90.子集II
topic="""
    给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

 

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""

# 目前采取的是再加入到结果集的时候去重
# 可不可以在遍历的时候去重呢，
# 试着用选和不选的方式来去重，当上一个元素和当前元素相等的时候，并且上一个元素被选了的时候，这个元素就只能选，不能不选了。
# 当上一个元素和当前元素相等的时候，并且上一个元素没有被选的时候，这个元素就可以选和不选都可以了。
# 但是这样只能控制两个元素的去重，如果是三个及以上的元素重复，就不对了
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=set()
        path=[]
        def dfs(ind):
            if tuple(path[:]) not in ans:
                ans.add(tuple(path[:]))
            for j in range(ind,n):
                # if j>0 and nums[j]==nums[j-1]:
                #     continue
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return list(ans)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        path=[]
        # 试着用选和不选的方式来去重，当上一个元素和当前元素相等的时候，并且上一个元素被选了的时候，这个元素就只能选，不能不选了。
        # 当上一个元素和当前元素相等的时候，并且上一个元素没有被选的时候，这个元素就可以选和不选都可以了。
        def dfs(ind):
            ans.append(path.copy())
            for j in range(ind,n):
                if j>ind and nums[j]==nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        path=[]
        # 当不选x的时候，那么后面所有等于x的数都不选，如果不跳过这些数，会导致 选x不选x 和 不选x选x 重复
        def dfs(ind):
            if ind==n:
                ans.append(path.copy())
                return
            # 选x
            x=nums[ind]
            path.append(x)
            dfs(ind+1)
            path.pop()

            # 不选
            ind+=1
            while ind<n and nums[ind]==x:
                ind+=1
            dfs(ind)
        dfs(0)
        return ans















