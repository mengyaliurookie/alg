
# 513.找树左下角的值
topic="""
    给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。

 

示例 1:



输入: root = [2,1,3]
输出: 1
示例 2:



输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 可以用层序遍历，因为这是分层的，怎么判断到达最后一层了，就是需要记录每一层第一个节点
        # 遍历完毕之后，就是最底层最左边的节点
        ans=None
        queue=deque()
        queue.append(root)
        while queue:
            n=len(queue)
            # print(n)
            for i in range(n):
                top=queue.popleft()
                if i==0:
                    ans=top.val
                if top.left:queue.append(top.left)
                if top.right:queue.append(top.right)
        return ans

# 112. 路径总和

topic="""
    给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。

 

示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        if root.left==None and root.right==None:
            if targetSum-root.val==0:
                return True
            else:
                return False
        left=self.hasPathSum(root.left,targetSum-root.val)
        right=self.hasPathSum(root.right,targetSum-root.val)
        if left or right:
            return True
        else:
            return False

# 106.从中序与后序遍历序列构造二叉树
topic="""
    给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

 

示例 1:


输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
示例 2:

输入：inorder = [-1], postorder = [-1]
输出：[-1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 后序遍历，最后一个节点是根节点
        # 中序遍历根节点在中间
        # 可以利用后序遍历先找到根节点，然后去中序遍历中找到根节点，进而可以找到左子树和右子树的长度，进而可以把问题分解为重构左子树和右子树
        if len(inorder) == 0:
            return None
        val = postorder.pop()
        ind = inorder.index(val)
        leftinorder = inorder[:ind]
        rightinorder = inorder[ind + 1:]
        leftpostorder = postorder[:len(leftinorder)]
        rightpostorder = postorder[len(leftinorder):]

        left = self.buildTree(leftinorder, leftpostorder)
        right = self.buildTree(rightinorder, rightpostorder)
        return TreeNode(val, left, right)

# 654.最大二叉树
topic="""
    给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

创建一个根节点，其值为 nums 中的最大值。
递归地在最大值 左边 的 子数组前缀上 构建左子树。
递归地在最大值 右边 的 子数组后缀上 构建右子树。
返回 nums 构建的 最大二叉树 。

 

示例 1：


输入：nums = [3,2,1,6,0,5]
输出：[6,3,5,null,2,0,null,null,1]
解释：递归调用如下所示：
- [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
        - 空数组，无子节点。
        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
            - 空数组，无子节点。
            - 只有一个元素，所以子节点是一个值为 1 的节点。
    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
        - 只有一个元素，所以子节点是一个值为 0 的节点。
        - 空数组，无子节点。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def findmax(nums):
            maxv = float('-inf')
            for i in nums:
                if i > maxv: maxv = i
            return maxv

        def dfs(nums):
            if len(nums) == 0:
                return None
            indexs = {v: i for i, v in enumerate(nums)}
            tem = findmax(nums)
            ind = indexs[tem]
            leftnums = nums[:ind]
            rightnums = nums[ind + 1:]
            left = dfs(leftnums)
            right = dfs(rightnums)
            return TreeNode(tem, left, right)

        return dfs(nums)

# 方法二：单调栈
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            cur = TreeNode(num)
            while stack and stack[-1].val < num:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur
            stack.append(cur)

        return stack[0]











