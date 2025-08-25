
# 450.删除二叉搜索树中的节点
topic="""
    给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
 

示例 1:



输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。


示例 2:

输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
示例 3:

输入: root = [], key = 0
输出: []

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 删除节点的话，需要记录父节点，还需要涉及替换的步骤
        if root == None: return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # 当前节点就是要删除的节点
            # 如果只有一个子节点或者没有子节点
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            # 如果都有，则找到右子树的最小值
            rpre = root
            rroot = root.right
            while rroot.left:
                rpre = rroot
                rroot = rroot.left
            # 替换节点
            # 先把最小值节点删除
            if rpre == root:
                rpre.right = rroot.right
            else:
                rpre.left = rroot.right
            # 然后替换
            rroot.left = root.left
            rroot.right = root.right
            root = rroot
        return root


# 669. 修剪二叉搜索树

topic="""
    给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

 

示例 1：


输入：root = [1,0,2], low = 1, high = 2
输出：[1,null,2]
示例 2：


输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
输出：[3,2,null,1]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 当当前节点不在范围内的时候，如果root.val<low，则左子树可以都排除
        # 如果root.val>high，则右子树可以都排除
        if root is None:
            return None
        if root.val >= low and root.val <= high:
            # 则保留当前节点
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        elif root.val < low:
            # 则进入右子树
            return self.trimBST(root.right, low, high)
        else:
            # 则进入左子树
            return self.trimBST(root.left, low, high)
        return root

# 108.将有序数组转换为二叉搜索树
topic="""
    给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

 

示例 1：


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：


输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
 

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 平衡二叉搜索树的意思就是左右子树的高度相差不超过1
        # 因为是构造，所以，可以每次找中间节点，这样转化为一个子问题
        if len(nums) == 0:
            return None
        # 找到中间节点，然后构造父节点，然后把数组一分为二
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid], self.sortedArrayToBST(nums[0:mid]), self.sortedArrayToBST(nums[mid + 1:]))
        return root


# 538.把二叉搜索树转换为累加树
topic="""
    给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同

 

示例 1：



输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
示例 2：

输入：root = [0,null,1]
输出：[1,null,1]
示例 3：

输入：root = [1,0,2]
输出：[3,3,2]
示例 4：

输入：root = [3,2,4,1]
输出：[7,9,4,10]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 中序遍历访问的顺序是二叉搜索树的递增序列
        # 而这道题的需要递减序列
        # 访问顺序为右中左
        # 需要返回的是当前节点的值
        pre = 0

        # ans=[]
        def dfs(root):
            if root is None:
                return
            dfs(root.right)
            nonlocal pre
            # pre代表的是上一个节点的值，当前节点的值加上上一个节点的值，就是当前节点的值
            root.val = root.val + pre
            pre = root.val
            dfs(root.left)

        dfs(root)
        # print(ans)
        return root








