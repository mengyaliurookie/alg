# dijkstra（朴素版）精讲
# 47. 参加科学大会（第六期模拟笔试）
topic="""
题目描述
小明是一位科学家，他需要参加一场重要的国际科学大会，以展示自己的最新研究成果。

小明的起点是第一个车站，终点是最后一个车站。然而，途中的各个车站之间的道路状况、交通拥堵程度以及可能的自然因素（如天气变化）等不同，这些因素都会影响每条路径的通行时间。

小明希望能选择一条花费时间最少的路线，以确保他能够尽快到达目的地。

输入描述
第一行包含两个正整数，第一个正整数 N 表示一共有 N 个公共汽车站，第二个正整数 M 表示有 M 条公路。 

接下来为 M 行，每行包括三个整数，S、E 和 V，代表了从 S 车站可以单向直达 E 车站，并且需要花费 V 单位的时间。

输出描述
输出一个整数，代表小明从起点到终点所花费的最小时间。
输入示例
7 9
1 2 1
1 3 4
2 3 2
2 4 5
3 4 2
4 5 3
2 6 4
5 7 4
6 7 9
输出示例
12
提示信息
能够到达的情况：

如下图所示，起始车站为 1 号车站，终点车站为 7 号车站，绿色路线为最短的路线，路线总长度为 12，则输出 12。

不能到达的情况：

如下图所示，当从起始车站不能到达终点车站时，则输出 -1。

数据范围：

1 <= N <= 500;
1 <= M <= 5000;
"""
# 这属于最短路径问题，应该是可以采用动态规划的思路来解决
# 
import math
# 这是采用
"""
Floyd-Warshall 的核心思想

我们有一个 dp[i][j] 矩阵，表示 i 到 j 的最短距离。

初始化的时候：

dp[i][j] = w(i,j) （如果有边 i→j，权重是 w，否则是 ∞）。

dp[i][i] = 0。

然后做三重循环：

for k in range(1, n+1):          # 允许经过的中转点
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


含义：如果允许经过点 k，那么 i→j 的最短路要么是不经过 k 的旧值，要么是 i→k→j 的更短路径。

当所有 k 都遍历完后，dp[i][j] 就是 i 到 j 的最短路径。

🔹 举个例子

比如图：

1 → 2 (100)
1 → 3 (1)
3 → 4 (1)
4 → 2 (1)
2 → 5 (1)


初始化矩阵（∞ 表示不可达）：

dp[1][2] = 100
dp[1][3] = 1
dp[3][4] = 1
dp[4][2] = 1
dp[2][5] = 1


跑 Floyd 后：

dp[1][5] 会被更新成 4（1→3→4→2→5）。

这样就不会漏掉了 ✅。

🔹 总结

如果你只想要 1 → n，用 Dijkstra 就够快了。

如果你要“任意两点间”的最短路（比如你说的 dp[4][5]），那就用 Floyd-Warshall。

要不要我帮你写一个 完整的 Floyd-Warshall Python 代码模板，你以后就能直接套用？
"""
# 这是用来求解任意两点间的最短路径，时间复杂度是O(n^3)，空间复杂度是O(n^2)
# 但是用来求解两点之间的最短路径的话会超时
def main():
    # 初始条件是，到达1节点最短的路径是0
    # 然后从1节点出发，可以到达的点的最短路径就是各自的
    # 递推公式是可以到达与当前节点连接的各个点，加上各个点到当前点的路径值，中的最小值，就是可以达到当前节点的最短路径值
    n,m=map(int,input().strip().split())
    graph=[[0]*(n+1) for _ in range(n+1)]
    dp=[[math.inf]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        i,j,v=map(int,input().strip().split())
        graph[i][j]=v
        dp[i][j]=v
    for i in range(1,n+1):
        dp[i][i]=0
    
    for k in range(1,n+1):
        # k表示可以经过的中间点
        for i in range(1,n+1):
            if dp[i][k]==math.inf:
                continue
            for j in range(1,n+1):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
    if dp[1][n]==math.inf:
        print(-1)
    else:
        print(dp[1][n])

# 这种只能用来求解有向无环图的最短路径问题，对于一般性的正权重的图，
# 可以采用dijkstra算法来解决
import math
from functools import lru_cache

def main():
    # 初始条件是，到达1节点最短的路径是0
    # 然后从1节点出发，可以到达的点的最短路径就是各自的
    # 递推公式是可以到达与当前节点连接的各个点，加上各个点到当前点的路径值，中的最小值，就是可以达到当前节点的最短路径值
    n,m=map(int,input().strip().split())
    graph=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        i,j,v=map(int,input().strip().split())
        graph[i][j]=v

    visiting = set()
    @lru_cache(maxsize=None)
    def dfs(i):
        if i in visiting:
            return math.inf
        if i==1:
            return 0
        visiting.add(i)
        dis=math.inf
        for j in range(1,n+1):
            if graph[j][i]>0:
                dis=min(dis,dfs(j)+graph[j][i])
        visiting.remove(i)
        return dis
    ans=dfs(n)
    if ans==math.inf:
        print(-1)
    else:
        print(ans)

# dijkstra算法
# 用一个数组来表示从源点到每个点的最短距离
# 
import math
from functools import lru_cache

def main():
    # 初始条件是，到达1节点最短的路径是0
    # 然后从1节点出发，可以到达的点的最短路径就是各自的
    # 递推公式是可以到达与当前节点连接的各个点，加上各个点到当前点的路径值，中的最小值，就是可以达到当前节点的最短路径值
    n,m=map(int,input().strip().split())
    graph=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        i,j,v=map(int,input().strip().split())
        graph[i][j]=v

    # dijkstra算法
    mindist=[math.inf]*(n+1)
    visited=[False]*(n+1)
    # 步骤先把1节点更新为0
    # 表示从1出发到达1最近距离为0
    # 然后从1节点开始出发更新从1节点可以达到的节点的最近距离
    # 然后标记1为已经访问
    mindist[1]=0
    for i in range(1,n+1):
        # 选没有被访问过的，且距离源点最近的点
        minNext=math.inf
        nexti=i
        for j in range(1,n+1):
            if not visited[j] and mindist[j]<minNext:
                minNext=mindist[j]
                nexti=j
        # 标记这个最近的点为已经访问过
        visited[nexti]=True
        # 更新这个点可以到达的点
        for j in range(1,n+1):
            if not visited[j] and graph[nexti][j]>0:
                mindist[j]=min(mindist[nexti]+graph[nexti][j],mindist[j])
    if mindist[n]==math.inf:
        print(-1)
    else:
        print(mindist[-1])






