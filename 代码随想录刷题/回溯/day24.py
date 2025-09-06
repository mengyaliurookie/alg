
# 332.重新安排行程
topic="""
    给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。

所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。

例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。

 

示例 1：


输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
输出：["JFK","MUC","LHR","SFO","SJC"]
示例 2：


输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
"""
# 这种写法会超时，
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 一种暴力的方式是把所有情况进行全排列，然后找出一条是从JFK出发的，并且可以走通的路
        n=len(tickets)
        ans=[]
        path=[]
        def isvalid(tickets):
            # 前一张票的终点，是后一张票的起点，否则不是有效的形成组合
            ans=True
            for i,v in enumerate(tickets):
                if i>0:
                    if v[0]!=tickets[i-1][1]:
                        ans=False
                        break
            return ans
        def getans(tickets):
            ans=[]
            n=len(tickets)
            for i,v in enumerate(tickets):
                if i<n-1:
                    ans.append(v[0])
                else:
                    ans.extend(v)
            return ans
        used=[False]*n
        def dfs(d,last):
            if d==n:
                if path[0][0]=='JFK' and isvalid(path):
                    ans.append(getans(path))
                return
            # if d==1 and last[0]!='JFK':
            #     return
            for i in range(n):
                if d==0 and tickets[i][0]!='JFK':
                    continue
                # 剪枝，当前一张票和后一张票不能成功连通就直接跳过
                if last and last[1]!=tickets[i][0]:
                    continue
                if not used[i]:
                    used[i]=True
                    path.append(tickets[i])
                    dfs(d+1,tickets[i])
                    path.pop()
                    used[i]=False
        dfs(0,None)
        # print(ans)
        ans.sort()
        return ans[0]

# 改进了，但是还是会超时
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 一种暴力的方式是把所有情况进行全排列，然后找出一条是从JFK出发的，并且可以走通的路
        n = len(tickets)
        ans = []
        path = ['JFK']
        # 直接全排列的方式会超时
        # 看了部分题解的大概用了什么数据结构，所以尝试改进一下
        # 用一个字典，key是各个点，然后v是从key出发可以到达的点
        dic = defaultdict(list)
        for t in tickets:
            dic[t[0]].append(t[1])
        # 然后对字典中的列表进行排序
        used = {}
        for k, v in dic.items():
            dic[k].sort()
            used[k] = [False] * len(v)
        print(dic)

        # 然后从JFK开始进行dfs
        # 还要避免重复使用同一张票
        def dfs(i, key):
            if i == n and not ans:
                ans.append(path[:])
                return
            if ans: return
            layer = dic[key]
            m = len(layer)
            for j in range(m):
                if not used[key][j]:
                    used[key][j] = True
                    path.append(layer[j])
                    dfs(i + 1, layer[j])
                    path.pop()
                    used[key][j] = False

        dfs(0, 'JFK')
        return ans[0]

# 这样才不会超时，核心关键是有明确的入队时机，这样就可以遍历一次就可以了。
# 而回溯的方式，只有在最后的时候才会判断，或者中间加一些剪枝，但是如果先走到死胡同，那还是会回溯到正确的位置，然后走，最终还是会走一遍之前走的死胡同。所以会重复走。
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 一种暴力的方式是把所有情况进行全排列，然后找出一条是从JFK出发的，并且可以走通的路
        # 直接全排列的方式会超时
        # 看了部分题解的大概用了什么数据结构，所以尝试改进一下
        # 用一个字典，key是各个点，然后v是从key出发可以到达的点
        dic=defaultdict(list)
        for t in tickets:
            dic[t[0]].append(t[1])
        # 然后对字典中的列表进行排序
        for k,v in dic.items():
            dic[k].sort(reverse=True)
        # 然后从JFK开始进行dfs
        # 还要避免重复使用同一张票
        queue=deque()
        def dfs(key):
            while dic[key]:
                nextnode=dic[key].pop()
                dfs(nextnode)
            queue.appendleft(key)
        dfs('JFK')
        return list(queue)


# 51. N皇后
topic="""
    按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位

输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
"""

# 这基本是自己完成的思路，但是代码写的比较差，然后中间借助ai调试了很多次边界问题。
# 还有一个重要的错误就是，之前是用True和False来表示是否访问过，但是这样会出错，因为回溯的时候会错误的取消掉上层的访问状态。因为同一个点会被不同的皇后访问，所以需要用计数的方式来表示访问过
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 尝试遍历第一个皇后可以选择的位置1-n，当选定之后，会把地图划分为很多区域（区域必须是连通的）
        # 当区域大小退化为1或者2,3,4的时候，那么这个区域只能放一个
        # 当选定一个位置之后，把其他位置全部标记为不可访问，
        # 每行必须有一个，每列必须有一个。不然必会出现两个在同一行或者同一列的问题，这必然会导致相互攻击的问题
        # 可以先看看当一行选定之后，对下一行的影响
        dp = [[0] * n for _ in range(n)]
        ans = []
        path = []

        def tag(row, col):
            # 把行列标记为不可访问
            for i in range(n):
                dp[row][i] += 1
                dp[i][col] += 1
            # 把斜着的标记为不可访问
            # row加col加，row加col减
            # row减col加，row减col减
            # 四种情况
            # row减col加
            rowj = row
            colj = col
            while rowj >= 0 and colj < n:
                dp[rowj][colj] += 1
                rowj -= 1
                colj += 1

            # row减col减
            rowj = row
            colm = col
            while rowj >= 0 and colm >= 0:
                dp[rowj][colm] += 1
                rowj -= 1
                colm -= 1

            # row加col减
            rowj = row
            colm = col
            while rowj < n and colm >= 0:
                dp[rowj][colm] += 1
                rowj += 1
                colm -= 1

            # row加col加
            rowj = row
            colm = col
            while rowj < n and colm < n:
                dp[rowj][colm] += 1
                rowj += 1
                colm += 1

        def untag(row, col):
            # 把行列标记为不可访问
            for i in range(n):
                dp[row][i] -= 1
                dp[i][col] -= 1
            # 把斜着的标记为不可访问
            # row加col加，row加col减
            # row减col加，row减col减
            # 四种情况
            # row减col加
            rowj = row
            colj = col
            while rowj >= 0 and colj < n:
                dp[rowj][colj] -= 1
                rowj -= 1
                colj += 1

            # row减col减
            rowj = row
            colm = col
            while rowj >= 0 and colm >= 0:
                dp[rowj][colm] -= 1
                rowj -= 1
                colm -= 1

            # row加col减
            rowj = row
            colm = col
            while rowj < n and colm >= 0:
                dp[rowj][colm] -= 1
                rowj += 1
                colm -= 1

            # row加col加
            rowj = row
            colm = col
            while rowj < n and colm < n:
                dp[rowj][colm] -= 1
                rowj += 1
                colm += 1

        def dfs(row):
            if row == n:
                ans.append(path[:])
                return
            # 选定列
            for col in range(n):
                if dp[row][col] != 0: continue
                path.append(col)
                # 选定某一列
                # 需要标记整个棋盘
                tag(row, col)
                dfs(row + 1)
                untag(row, col)
                path.pop()

        def getans(ans):
            result = []
            for row in ans:  # 每个 row 是一个解，如 [0,1] 或 [1,0]
                board = []
                for col_index in row:
                    s = '.' * col_index + 'Q' + '.' * (n - col_index - 1)
                    board.append(s)
                result.append(board)
            return result

        dfs(0)
        # print(ans)
        return getans(ans)


# 37. 解数独
topic="""
    编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
解释：输入的数独如上图所示，唯一有效的解决方案如下所示：

提示：

board.length == 9
board[i].length == 9
board[i][j] 是一位数字或者 '.'
题目数据 保证 输入数独仅有一个解
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 需要遍历一遍这个数独表，然后找出每个点可以安排的数字，然后在每次选定一个数字之后，要更新这个点可以影响到的点的状态，
        #
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.': continue
                    for k in range(1, 10):
                        if isValid(i, j, board, str(k)):
                            board[i][j] = str(k)
                            if dfs(board): return True
                            board[i][j] = '.'
                    return False
            return True

        def isValid(row, col, board, val):
            # 查看val是不是已经存在于以row，col为坐标的三个条件，即行，列，3X3宫格内，如果存在就返回False
            # 否则就返回True
            # 行
            for c in range(9):
                if board[row][c] == val:
                    return False
            # 列
            for r in range(9):
                if board[r][col] == val:
                    return False
            # 3X3宫格
            # 确定当前节点属于哪个3X3宫内部
            startrow = int(row / 3) * 3
            startcol = int(col / 3) * 3
            for i in range(startrow, startrow + 3):
                for j in range(startcol, startcol + 3):
                    if board[i][j] == val:
                        return False
            return True

        return dfs(board)













