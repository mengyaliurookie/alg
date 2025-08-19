
# 222.完全二叉树的节点个数

topic="""
    给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层（从第 0 层开始），则该层包含 1~ 2h 个节点。

 

示例 1：


输入：root = [1,2,3,4,5,6]
输出：6
示例 2：

输入：root = []
输出：0
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 可以利用层序遍历的方式，可以利用倒数第二层就计算出来，这样可以少遍历一层，在数据多的时候，还是挺有用
        queue=deque()
        if root is None:return 0
        queue.append(root)
        layer=0
        ans=1
        while queue:
            n=len(queue)
            for i in range(n):
                top=queue.popleft()
                if top.left:
                    queue.append(top.left)
                    ans+=1
                if top.right:
                    queue.append(top.right)
                    ans+=1
        return ans

# 进阶方法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 可以利用层序遍历的方式，可以利用倒数第二层就计算出来，这样可以少遍历一层，在数据多的时候，还是挺有用
        def height(root):
            height = 0
            while root:
                root = root.left
                height += 1
            return height

        # 空树，节点数为0
        if root == None: return 0
        leftHeight = height(root.left)
        rightHeight = height(root.right)

        # 如果左子树的深度=右子树的深度，左子树为满二叉树
        # 节点数=左子树的深度+右子树的深度+根节点
        if leftHeight == rightHeight:
            return (2 ** leftHeight - 1) + self.countNodes(root.right) + 1
        # 如果左子树的深度>右子树的深度，右子树为满二叉树
        # 节点数=左子树的深度+右子树的深度+根节点
        else:
            return (2 ** rightHeight - 1) + self.countNodes(root.left) + 1


# 110.平衡二叉树
topic="""
    给定一个二叉树，判断它是否是 平衡二叉树  

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True
        def dfs(root):
            if root==None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            if abs(left-right)>1:
                nonlocal ans
                ans=False
            return max(left,right)+1
        dfs(root)
        return ans

# 方法二

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root):
            if root==None:
                return 0
            left=get_height(root.left)
            right=get_height(root.right)
            if left==-1 or right==-1 or abs(left-right)>1:
                return -1
            return max(left,right)+1
        return get_height(root)!=-1


# 257. 二叉树的所有路径
topic="""
    给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。

 
示例 1：


输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = [str(root.val)]

        def dfs(root, path):
            if root.left == None and root.right == None:
                ans.append(path[:])
            if root.left:
                path.append(str(root.left.val))
                dfs(root.left, path)
                path.pop()
            if root.right:
                path.append(str(root.right.val))
                dfs(root.right, path)
                path.pop()

        dfs(root, path)
        ans = ["->".join(i) for i in ans]
        return ans

# 方法二，直接拼接字符串，因为字符串是不可变对象，所以不用回溯
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = "{}".format(root.val)

        def dfs(root, path):
            if root.left == None and root.right == None:
                ans.append(path[:])
            if root.left:
                dfs(root.left, path + "->{}".format(root.left.val))
            if root.right:
                dfs(root.right, path + "->{}".format(root.right.val))

        dfs(root, path)
        # ans=["->".join(i) for i in ans]
        return ans


# 404.左叶子之和
topic="""
    给定二叉树的根节点 root ，返回所有左叶子之和。

 

示例 1：



输入: root = [3,9,20,null,null,15,7] 
输出: 24 
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
示例 2:

输入: root = [1]
输出: 0
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 判定条件，当遇到None返回
        # 访问左节点不为None，且左节点的左右节点都为None的时候，需要统计
        ans = 0

        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            dfs(root.right)
            if root.left and root.left.left == None and root.left.right == None:
                nonlocal ans
                ans += root.left.val

        dfs(root)
        return ans




