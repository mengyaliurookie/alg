
# 226.翻转二叉树
topic="""
    给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

 

示例 1：



输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 可以用后序遍历来处理
        def dfs(root):
            if root is None: return
            dfs(root.left)
            dfs(root.right)
            root.left, root.right = root.right, root.left

        dfs(root)
        return root

# 101. 对称二叉树

topic="""
    给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSim(left,right):
            if left is None or right is None:
                return left==right
            lleft=left.left
            lright=left.right
            rleft=right.left
            rright=right.right
            res1=isSim(lleft,rright)
            res2=isSim(lright,rleft)
            return res1 and res2 and left.val==right.val
        left=root.left
        right=root.right
        return isSim(left,right)

# 104.二叉树的最大深度
topic="""
    给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

 

示例 1：



 

输入：root = [3,9,20,null,null,15,7]
输出：3
示例 2：

输入：root = [1,null,2]
输出：2
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 后序遍历，需要判断左右节点的返回值，到达叶节点就返回0
        def dfs(root):
            if root is None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            return max(left,right)+1
        return dfs(root)


# 111.二叉树的最小深度

topic="""
    给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
"""

# 坑
# 需要注意只有左右两个节点都为None，才是叶节点
# 不然单链还是需要返回

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 是不是把最大值判定改成最小值就可以了，试一下
        # 好像不可以，因为这里的叶子节点是指左右子树都为None
        if root is None: return 0

        def dfs(root):
            # 如果是叶节点直接返回0
            if root.left is None and root.right is None:
                return 0
            else:
                # 否则需要返回左节点或者右节点，加一
                if root.left is None:
                    return dfs(root.right) + 1
                elif root.right is None:
                    return dfs(root.left) + 1
            # 此时都不为None
            left = dfs(root.left)
            right = dfs(root.right)
            return min(left, right) + 1

        return dfs(root) + 1


