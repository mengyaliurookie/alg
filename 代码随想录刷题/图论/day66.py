# Floyd 算法精讲
topic="""
97. 小明逛公园
题目描述
小明喜欢去公园散步，公园内布置了许多的景点，相互之间通过小路连接，小明希望在观看景点的同时，能够节省体力，走最短的路径。 



给定一个公园景点图，图中有 N 个景点（编号为 1 到 N），以及 M 条双向道路连接着这些景点。每条道路上行走的距离都是已知的。



小明有 Q 个观景计划，每个计划都有一个起点 start 和一个终点 end，表示他想从景点 start 前往景点 end。由于小明希望节省体力，他想知道每个观景计划中从起点到终点的最短路径长度。 请你帮助小明计算出每个观景计划的最短路径长度。

输入描述
第一行包含两个整数 N, M, 分别表示景点的数量和道路的数量。 

接下来的 M 行，每行包含三个整数 u, v, w，表示景点 u 和景点 v 之间有一条长度为 w 的双向道路。 

接下里的一行包含一个整数 Q，表示观景计划的数量。 

接下来的 Q 行，每行包含两个整数 start, end，表示一个观景计划的起点和终点。

输出描述
对于每个观景计划，输出一行表示从起点到终点的最短路径长度。如果两个景点之间不存在路径，则输出 -1。
输入示例
7 3
2 3 4
3 6 6
4 7 8
2
2 3
3 4
输出示例
4
-1
提示信息
从 2 到 3 的路径长度为 4，3 到 4 之间并没有道路。

1 <= N, M, Q <= 1000.

1 <= w <= 10000.
"""
import math

def main():
    
    n,m=map(int,input().strip().split())
    
    dp=[[math.inf]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        i,j,v=map(int,input().strip().split())
        dp[i][j]=v
        dp[j][i]=v
    t=int(input().strip())
    res=[]
    for _ in range(t):
        res.append(list(map(int,input().strip().split())))
    for i in range(1,n+1):
        dp[i][i]=0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
    for i,j in res:
        if dp[i][j]==math.inf:
            print(-1)           
        else:
            print(dp[i][j])

if __name__=="__main__":
    main()

# A * 算法精讲 （A star算法）
topic = """
127. 骑士的攻击
题目描述
在象棋中，马和象的移动规则分别是“马走日”和“象走田”。现给定骑士的起始坐标和目标坐标，要求根据骑士的移动规则，计算从起点到达目标点所需的最短步数。



棋盘大小 1000 x 1000（棋盘的 x 和 y 坐标均在 [1, 1000] 区间内，包含边界）

输入描述
第一行包含一个整数 n，表示测试用例的数量，1 <= n <= 100。

接下来的 n 行，每行包含四个整数 a1, a2, b1, b2，分别表示骑士的起始位置 (a1, a2) 和目标位置 (b1, b2)。

输出描述
输出共 n 行，每行输出一个整数，表示骑士从起点到目标点的最短路径长度。
输入示例
6
5 2 5 4
1 1 2 2
1 1 8 8
1 1 8 7
2 1 3 3
4 6 4 6
输出示例
2
4
6
5
1
0
提示信息
骑士移动规则如图，红色是起始位置，黄色是骑士可以走的地方。
"""
# 利用广度搜索算法求解，时间会超时
from collections import deque


def main():
    global graph
    n = int(input())
    examples = [list(map(int, input().strip().split())) for _ in range(n)]
    for x1, y1, x2, y2 in examples:
        bfs(x1, y1, x2, y2)
        print(graph[x2][y2])


graph = []


def bfs(x1, y1, x2, y2):
    global graph
    graph = [[0] * 1001 for _ in range(1001)]
    rang = [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1]]
    queue = deque()
    queue.append((x1, y1))
    # graph[x1][y1]=1
    while queue:
        s1, s2 = queue.popleft()
        if s1 == x2 and s2 == y2:
            break
        for i, j in rang:
            nexti = s1 + i
            nextj = s2 + j
            if 1 <= nexti <= 1000 and 1 <= nextj <= 1000 and not graph[nexti][nextj]:
                graph[nexti][nextj] = graph[s1][s2] + 1
                queue.append((nexti, nextj))


# A* 算法
import heapq

n = int(input())

moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]


def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def bfs(start, end):
    q = [(distance(start, end), start)]
    step = {start: 0}

    while q:
        d, cur = heapq.heappop(q)
        if cur == end:
            return step[cur]
        for move in moves:
            new = (move[0] + cur[0], move[1] + cur[1])
            if 1 <= new[0] <= 1000 and 1 <= new[1] <= 1000:
                step_new = step[cur] + 1
                if step_new < step.get(new, float('inf')):
                    step[new] = step_new
                    heapq.heappush(q, (distance(new, end) + step_new, new))
    return False


for _ in range(n):
    a1, a2, b1, b2 = map(int, input().split())
    print(bfs((a1, a2), (b1, b2)))
