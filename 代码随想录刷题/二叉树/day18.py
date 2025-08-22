
# 501.二叉搜索树中的众数
topic="""
    给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 任意顺序 返回。

假定 BST 满足如下定义：

结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树
 

示例 1：


输入：root = [1,null,2,2]
输出：[2]
示例 2：

输入：root = [0]
输出：[0]
 

提示：

树中节点的数目在范围 [1, 104] 内
-105 <= Node.val <= 105

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            nonlocal ans
            ans.append(root.val)
            dfs(root.right)

        dfs(root)
        # print(ans)
        coun = Counter()
        for i in ans:
            coun[i] += 1
        maxn = sorted(coun.values())[-1]
        answ = []
        for k, v in coun.items():
            if coun[k] == maxn: answ.append(k)
        return answ

# 236. 二叉树的最近公共祖先
topic="""
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

 

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 可以用后序遍历的方式，判断左右节点的返回值，当节点值等于p和q的时候就返回当前节点，否则返回None
        # 当左右节点返回值都不为None的时候就返回当前节点，否则返回左右节点返回值不为None的，或者返回None
        # 同时在当前节点判断，左右子树返回的节点值是不是p和q，如果第一次是就返回这个节点。
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left or right:
            return left if left else right
        return None


# 235. 二叉搜索树的最近公共祖先
topic="""
    给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



 

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 可以利用二叉搜索的有序性，进行剪枝
        # 剪枝的规则是，当p和q的值都大于当前节点，则一定不在左子树
        # 同理当p和q的值都小于当前节点，则一定不在右子树
        # 当p和q位于当前节点两侧，则按照正常的情况
        if root in (None,p,q):
            return root
        if root.val>p.val and root.val>q.val:
            right=None
            left=self.lowestCommonAncestor(root.left,p,q)
        elif root.val<p.val and root.val<q.val:
            left=None
            right=self.lowestCommonAncestor(root.right,p,q)
        else:
            left=self.lowestCommonAncestor(root.left,p,q)
            right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 可以利用二叉搜索的有序性，进行剪枝
        # 剪枝的规则是，当p和q的值都大于当前节点，则一定不在左子树
        # 同理当p和q的值都小于当前节点，则一定不在右子树
        # 当p和q位于当前节点两侧，则按照正常的情况
        x=root.val
        if p.val<x and q.val<x:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>x and q.val>x:
            return self.lowestCommonAncestor(root.right,p,q)
        return root


# 701.二叉搜索树中的插入操作
topic="""
    给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

 

示例 1：


输入：root = [4,2,7,1,3], val = 5
输出：[4,2,7,1,3,5]
解释：另一个满足题目要求可以通过的树是：

示例 2：

输入：root = [40,20,60,10,30,50,70], val = 25
输出：[40,20,60,10,30,50,70,null,null,25]
示例 3：

输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
输出：[4,2,7,1,3,5]
    
"""











