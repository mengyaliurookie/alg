
# 617.合并二叉树
topic="""
    给你两棵二叉树： root1 和 root2 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

注意: 合并过程必须从两个树的根节点开始。

 

示例 1：


输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
输出：[3,4,5,5,4,null,7]
示例 2：

输入：root1 = [1], root2 = [1,2]
输出：[2,2]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 返回条件
        if root1 == None and root2 == None:
            return None

        if root1 and root2:
            left = self.mergeTrees(root1.left, root2.left)
            right = self.mergeTrees(root1.right, root2.right)
            newTree = TreeNode(root1.val + root2.val, left, right)
        if root1 and not root2:
            left = self.mergeTrees(root1.left, None)
            right = self.mergeTrees(root1.right, None)
            newTree = TreeNode(root1.val, left, right)
        if root2 and not root1:
            left = self.mergeTrees(None, root2.left)
            right = self.mergeTrees(None, root2.right)
            newTree = TreeNode(root2.val, left, right)
        return newTree

# 简洁的写法，可以剪枝
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 返回条件
        if root1 is None: return root2
        if root2 is None: return root1
        return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left),
                        self.mergeTrees(root1.right, root2.right))


# 700.二叉搜索树中的搜索

topic="""
    给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

 

示例 1:



输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]
示例 2:


输入：root = [4,2,7,1,3], val = 5
输出：[]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root


# 98.验证二叉搜索树
topic="""
    给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 严格小于 当前节点的数。
节点的右子树只包含 严格大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
 

示例 1：


输入：root = [2,1,3]
输出：true
示例 2：


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 可以利用中序遍历的性质，看看中序遍历得到的数组是不是有序的
        ans=[]
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            nonlocal ans
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        n=len(ans)
        answer=True
        for i in range(1,n):
            if ans[i-1]>=ans[i]:
                answer=False
                break
        return answer

# 其实按照这个思路的话，在中序遍历的过程中，只要判断当前节点的值是否小于前一个节点的值，就可以判断是否是二叉搜索树了，但是怎么获取前一个节点的值呢？
# 返回的值可以是一个列表，列表的第一个值是前一个节点，第二个值是结果值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 可以利用中序遍历的性质，看看中序遍历得到的数组是不是有序的
        ans=[]
        def dfs(root):
            if root is None:
                return True
            left=dfs(root.left)
            if not left:return False
            nonlocal ans
            if ans:
                if root.val<=ans[-1]: return False
            ans.append(root.val)
            right=dfs(root.right)
            return right
        return dfs(root)

# 530.二叉搜索树的最小绝对差
topic="""
    给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。

 

示例 1：


输入：root = [4,2,6,1,3]
输出：1
示例 2：


输入：root = [1,0,48,null,null,12,49]
输出：1
 

提示：

树中节点的数目范围是 [2, 104]
0 <= Node.val <= 105
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = -100000
        ans = inf

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            nonlocal pre
            nonlocal ans
            ans = min(root.val - pre, ans)
            pre = root.val
            dfs(root.right)

        dfs(root)
        return ans









