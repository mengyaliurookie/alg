
# 56. 合并区间
topic="""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
示例 3：

输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=intervals
        l.sort()
        ln=len(l)
        fir=l[0][0]
        sec=l[0][1]
        ans=[]
        for f in range(1,ln):
            if l[f][0]<=sec:
                sec=max(l[f][1],sec)
            else:
                ans.append([fir,sec])
                fir=l[f][0]
                sec=l[f][1]
        ans.append([fir,sec])
        return ans

# 738.单调递增的数字
topic="""
当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。

给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

 

示例 1:

输入: n = 10
输出: 9
示例 2:

输入: n = 1234
输出: 1234
示例 3:

输入: n = 332
输出: 299
"""
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 从后往前遍历，当出现逆序的时候，那么
        tem=[]
        fn=n
        while n:
            tem.append(n%10)
            n=n//10
        # print(tem)
        nl=len(tem)
        isnine=-1
        for i in range(1,nl):
            if tem[i]>tem[i-1]:
                tem[i]=tem[i]-1
                isnine=i-1
        ans=None
        if isnine==-1:
            ans=fn
        else:
            for i in range(isnine+1):
                tem[i]=9
            ans=0
            while tem:
                t=tem.pop()
                ans=ans*10+t
        return ans


# 968.监控二叉树
topic="""
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。

 

示例 1：



输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
示例 2：



输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 感觉要传递的是子节点是不是被监控了，这样才真的会影响当前节点的决策
        # 如果有一个没有被监控，那么此节点就必然是摄像头，这样才能保证子节点会被监控到，不然就漏了一个，就要加一
        # 如果都被监控了，那么没必要考虑子节点了，只考虑自己是不是应该是摄像头，默认应该不是，然后传递未被监控给父节点，然后没有父节点了，那么就最后加一个1，如果还有父节点，那就交给父节点来决策了。
        if root.left == None and root.right == None: return 1
        ans = 0

        def dfs(root):
            # 如果节点为空，那么需要向上传递为节点已经被监控了
            if root is None:
                return True
            left = dfs(root.left)
            right = dfs(root.right)

            # 如果都被监控了
            if left and right:
                # 那么返回False，表示当前节点不需要立即被监控，看情况
                # 还需要判断左右子节点是有一个是摄像头吗
                if root.left:
                    if root.left.val == 1:
                        return True
                if root.right:
                    if root.right.val == 1:
                        return True
                return False
            else:
                # 如果有一个子节点没有被监控
                # 那么当前节点必须是摄像头，才能监控到子节点
                nonlocal ans
                ans += 1
                root.val = 1
                return True

        res = dfs(root)
        # print(res)
        if res:
            return ans
        else:
            if root.left:
                if root.left.val == 1:
                    return ans
            if root.right:
                if root.right.val == 1:
                    return ans
            return ans + 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 感觉要传递的是子节点是不是被监控了，这样才真的会影响当前节点的决策
        # 如果有一个没有被监控，那么此节点就必然是摄像头，这样才能保证子节点会被监控到，不然就漏了一个，就要加一
        # 如果都被监控了，那么没必要考虑子节点了，只考虑自己是不是应该是摄像头，默认应该不是，然后传递未被监控给父节点，然后没有父节点了，那么就最后加一个1，如果还有父节点，那就交给父节点来决策了。
        if root.left == None and root.right == None: return 1
        ans = 0

        def dfs(root):
            # 如果节点为空，那么需要向上传递为节点已经被监控了
            if root is None:
                return True
            left = dfs(root.left)
            right = dfs(root.right)

            # 如果都被监控了
            if left and right:
                # 那么返回False，表示当前节点不需要立即被监控，看情况
                # 还需要判断左右子节点是有一个是摄像头吗
                if root.left:
                    if root.left.val == 1:
                        return True
                if root.right:
                    if root.right.val == 1:
                        return True
                return False
            else:
                # 如果有一个子节点没有被监控
                # 那么当前节点必须是摄像头，才能监控到子节点
                # 同时要标记当前节点的值为1，表示当前节点是摄像头，这样在父节点判断的时候，可以再次深入到子节点进行判断
                nonlocal ans
                ans += 1
                root.val = 1
                return True

        res = dfs(root)
        # print(res)
        if res:
            return ans
        else:
            return ans + 1




