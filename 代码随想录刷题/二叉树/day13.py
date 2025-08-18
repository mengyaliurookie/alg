
# 递归版本前序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.traver(root,l)
        return l
    def traver(self,root,l):
        if root is None:
            return
        l.append(root.val)
        self.traver(root.left,l)
        self.traver(root.right,l)

# 递归版本中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self.travel(root, l)
        return l

    def travel(self, root, l):
        if root is None: return
        self.travel(root.left, l)
        l.append(root.val)
        self.travel(root.right, l)
# 递归版本后序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self.travel(root, l)
        return l

    def travel(self, root, l):
        if root is None: return
        self.travel(root.left, l)
        self.travel(root.right, l)
        l.append(root.val)



# 迭代版本的先序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        # 迭代版本，需要用到一个栈来保存函数调用过程
        stack=[]
        # 先把根节点入栈
        stack.append(root)
        while stack:
            # 先访问中间节点，需要弹出栈顶
            mid=stack.pop()
            if mid:
                l.append(mid.val)
                # 然后入栈，先入右节点，再入左节点，因为要先访问左节点
                stack.append(mid.right)
                stack.append(mid.left)
        return l


# 迭代版本的中序遍历，需要记录是不是访问过某个节点，也就是第二次访问才添加到结果中
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        # 迭代版本，中序遍历，左中右
        # 栈
        stack = []
        hasvisit = set()
        stack.append(root)
        while stack:
            # 入栈顺序应该是右中左，所以先把栈中元素弹出，然后把右节点入栈，然后把中间节点入栈，然后把左节点入栈，如果左节点为None的话，那么需要访问当前弹出的节点。
            top = stack.pop()
            # print(top)
            if top:
                # 如果当前节点不为None的话，那么需要判断它的左节点是不是None
                # 左节点不为None，并且左节点没有被访问过
                if top.left and top.left not in hasvisit:
                    # 如果左节点不是None的话，需要把右节点，当前节点，左节点入栈
                    stack.append(top.right)
                    stack.append(top)
                    stack.append(top.left)
                else:
                    # 还要分情况，如果是左节点已经被访问过，那么右节点其实已经入栈了
                    # 如果是左节点为空的话，还需要把右节点入栈
                    if not top.left:
                        if top.right: stack.append(top.right)
                        ans.append(top.val)
                        hasvisit.add(top)
                    else:
                        ans.append(top.val)
                        hasvisit.add(top)
        return ans


# 迭代版本的后序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        stack=[]
        # 可以访问当前节点的前提是，左右节点都已经被访问过，或者说，左右节点都是None
        hasvis=set()
        hasvis.add(None)
        stack.append(root)
        while stack:
          top=stack.pop()
          if top:
            if (top.left is None and top.right is None) or (top.left in hasvis and top.right in hasvis) :
              ans.append(top.val)
              hasvis.add(top)
            else:
              # 否则就需要入栈
              stack.append(top)
              stack.append(top.right)
              stack.append(top.left)
        return ans


# 二叉树的层序遍历
# 因为要分层，所以需要记录每一层的个数，然后用for循环的方式去访问当前层
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 二叉树的层序遍历，是需要用到队列的
        queue=deque()
        # 用双端队列来实现普通的队列的逻辑操作
        # 入队：append()
        # 出队：popleft()
        ans=[]
        if root is None:return ans
        queue.append(root)
        # 还需要分层，用什么来区分是哪一层呢
        while queue:
            size=len(queue)
            tem=[]
            for i in range(size):
                top=queue.popleft()
                if top:
                    tem.append(top.val)
                    if top.left:queue.append(top.left)
                    if top.right:queue.append(top.right)
            ans.append(tem)
        return ans


