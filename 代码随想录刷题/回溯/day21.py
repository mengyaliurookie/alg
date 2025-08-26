
# 第77题. 组合
topic="""
    给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

 

示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2：

输入：n = 1, k = 1
输出：[[1]]
 

提示：

1 <= n <= 20
1 <= k <= n
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtracking(start: int, k: int, path: List[int]):
            # 当k==0时，满足条件返回
            if k == 0:
                ans.append(path[:])
                return
            for i in range(start, n + 1):
                # 选当前节点
                path.append(i)
                backtracking(i + 1, k - 1, path)
                path.pop()
                # 不选当前节点
                # backtracking(i+1,k,path)

        backtracking(1, k, [])
        return ans



# 216.组合总和III
topic="""
    找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

 

示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。
示例 3:

输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtracking(start, k, n, path):
            # 必须有k个数
            if k == 0:
                if n == 0:
                    # 如果和为n添加到结果集中，否则就返回
                    ans.append(path[:])
                return
            # 需要遍历1到9
            for i in range(start, 10):
                path.append(i)
                backtracking(i + 1, k - 1, n - i, path)
                path.pop()

        backtracking(1, k, n, [])
        return ans

# 剪枝版本
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtracking(start, k, n, path):
            # 剪枝

            # 必须有k个数
            if k == 0:
                if n == 0:
                    # 如果和为n添加到结果集中，否则就返回
                    ans.append(path[:])
                return
            # 需要遍历1到9
            for i in range(start, 10):
                if n - i < 0:
                    break
                # 剪枝2: 剩余可选的数字个数不足
                if k > 9 - i + 1:
                    break
                path.append(i)
                backtracking(i + 1, k - 1, n - i, path)
                path.pop()

        backtracking(1, k, n, [])
        return ans


# 17.电话号码的字母组合
topic="""
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
 

提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        n=len(digits)
        ans=[]
        if n==0:return ans
        def dfs(ind,path):
            # ind从0开始表示digits的第几个数字
            if ind==n:
                if len(path)==n:
                    ans.append("".join(path))
                return
            # 外层循环表示有几个数字，内层循环表示分别选择数字对应的那个字符
            for i in range(ind,n):
                alps=dic[digits[i]]
                for j in alps:
                    path.append(j)
                    dfs(i+1,path)
                    path.pop()
        dfs(0,[])
        return ans

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        n = len(digits)
        ans = []
        if n == 0:
            return ans
        def dfs(ind, path):
            if ind == n:
                ans.append("".join(path))
                return
            alps = dic[digits[ind]]
            for j in alps:                 # 只处理当前这一位
                path.append(j)
                dfs(ind + 1, path)         # 递归处理下一位
                path.pop()
        dfs(0, [])
        return ans

# 39. 组合总和
topic="""
    给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

 

示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #
        candidates.sort()
        n=len(candidates)
        ans=[]
        def dfs(ind,target,path):
            # print(path)
            if target==0:
                ans.append(path[:])
                return
            if target<0:return
            for i in range(ind,n):
                if candidates[i]>target:
                    break
                path.append(candidates[i])
                dfs(i,target-candidates[i],path)
                path.pop()
        dfs(0,target,[])
        return ans













