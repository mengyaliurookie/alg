# 图的基本概念
# 节点集合，边集合，边是通过首尾节点的方式来表达的
# 图的种类：
# 有向图，无向图，加权有向图，加权无向图
# 度：
# 无向图中有几条边连接该节点，该节点就有几度。
# 有向图中，每个节点有出度和入度
# 连通性：表示图中任意两个节点之间是否存在路径
# 强连通图：任何两个节点是可以互相到达的，我们称之为强连通图。
# 连通分量：在无向图中的极大连通子图称之为该图的一个连通分量
# 强连通图：在有向图中极大强连通子图称之为该图的强连通分量
# 
# 图的存储方式
# 朴素存储
# 直接把所有边存起来
# 邻接矩阵
# 用一个二维数组来表示图，数组的行和列分别表示图的节点，数组的值表示节点之间的边的关系。
# 邻接表
# 使用数组+链表的方式来表示。
# 图的遍历方式：
# 基本是两大类：
# 深度优先搜索（dfs）
# 广度优先搜索（bfs）

# 深度优先搜索理论基础
# dfs搜素过程


# 98. 所有可达路径
topic="""
98. 可达路径
题目描述
给定一个有 n 个节点的有向无环图，节点编号从 1 到 n。请编写一个函数，找出并返回所有从节点 1 到节点 n 的路径。每条路径应以节点编号的列表形式表示。
输入描述
第一行包含两个整数 N，M，表示图中拥有 N 个节点，M 条边

后续 M 行，每行包含两个整数 s 和 t，表示图中的 s 节点与 t 节点中有一条路径

输出描述
输出所有的可达路径，路径中所有节点之间空格隔开，每条路径独占一行，存在多条路径，路径输出的顺序可任意。如果不存在任何一条路径，则输出 -1。

注意输出的序列中，最后一个节点后面没有空格！ 例如正确的答案是 `1 3 5`,而不是 `1 3 5 `， 5后面没有空格！

输入示例
5 5
1 3
3 5
1 2
2 4
4 5
输出示例
1 3 5
1 2 4 5
提示信息




用例解释：

有五个节点，其中的从 1 到达 5 的路径有两个，分别是 1 -> 3 -> 5 和 1 -> 2 -> 4 -> 5。

因为拥有多条路径，所以输出结果为：

1 3 5
1 2 4 5

或

1 2 4 5
1 3 5
都算正确。



数据范围：

图中不存在自环
图中不存在平行边
1 <= N <= 100
1 <= M <= 500
"""
import sys

res=[]
path=[1]

def main():
    # 获取节点个数和边的个数
    n,m=map(int,sys.stdin.readline().strip().split())
    # print(f"节点个数：{n}")
    # print(f"边的个数：{m}")
    # 用邻接数组的方式存储
    graph=[[] for _ in range(n+1)]
    for i in range(m):
        ni,nj=map(int,sys.stdin.readline().strip().split())
        graph[ni].append(nj)
    # graph=graph[1:]
    # print(f"graph: {graph}")

    def dfs(i):
        if i==n:
            # print(path[:])
            res.append(path[:])
            return
        for j in graph[i]:
            path.append(j)
            dfs(j)
            path.pop()
    dfs(1)
    # print(res)
    if res:
        for k in res:
            print(" ".join(map(str,k)))
    else:
        print(-1)  

if __name__=='__main__':
    main()

# 广度优先搜索理论基础
# 

# 99. 岛屿数量
topic="""
题目描述
给定一个由 1（陆地）和 0（水）组成的矩阵，你需要计算岛屿的数量。岛屿由水平方向或垂直方向上相邻的陆地连接而成，并且四周都是水域。你可以假设矩阵外均被水包围。

输入描述
第一行包含两个整数 N, M，表示矩阵的行数和列数。

后续 N 行，每行包含 M 个数字，数字为 1 或者 0。

输出描述
输出一个整数，表示岛屿的数量。如果不存在岛屿，则输出 0。
输入示例
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例
3
提示信息




根据测试案例中所展示，岛屿数量共有 3 个，所以输出 3。



数据范围：

1 <= N, M <= 50
"""
import sys
from collections import deque

# 广度优先搜索的方法
def main():
    # 获取行数和列数
    n,m=map(int,sys.stdin.readline().strip().split())
    graph=[]
    visited=[]
    for i in range(n):
        tem=list(map(int,sys.stdin.readline().strip().split()))
        graph.append(tem)
        visited.append([False]*m)
    # print(f"graph: {graph}")
    # print(f"visited: {visited}")
    queue=deque()
    # 广度优先搜索
    bac=[[0,1],[1,0],[-1,0],[0,-1]]
    # 表示上右下左四个邻接节点
    # 当某一个节点本身是岛屿，并且它的的上下左右四个相邻节点都是被访问过，或者是水的话，那么就岛屿加一
    # 只要是没有访问过的节点，就需要添加到队列中
    # 用来找某个节点的连通图，并且标记它们为已访问，这样可以把整个岛屿都标记了
    def bfs(i,j):
        queue.append((i,j))
        visited[0][0]=True
        while queue:
            # print(f"queue: {queue}")
            # 弹出队列里的首数据
            i,j=queue.popleft() 
            for k,p in enumerate(bac):
                temi=i+p[0]
                temj=j+p[1]
                # print(f"temi: {temi}")
                # print(f"temj: {temj}")
                if temi>=0 and temi<n and temj>=0 and temj<m:
                    # 满足边界条件
                    if not visited[temi][temj]:
                        if graph[temi][temj]==1:
                            visited[temi][temj]=True
                            queue.append((temi,temj))
            # print(f"isiso: {isiso}")
            # print(f"graph: {graph[i][j]}")
    # 这里需要遍历整个矩阵
    ans=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and not visited[i][j]:
                ans+=1
                bfs(i,j)
    print(ans)
if __name__=="__main__":
    main()

# 深度搜索版本
import sys
from collections import deque

def main():
    # 获取行数和列数
    n,m=map(int,sys.stdin.readline().strip().split())
    graph=[]
    visited=[]
    for i in range(n):
        tem=list(map(int,sys.stdin.readline().strip().split()))
        graph.append(tem)
        visited.append([False]*m)
    # print(f"graph: {graph}")
    # print(f"visited: {visited}")
    queue=deque()
    # 广度优先搜索
    bac=[[0,1],[1,0],[-1,0],[0,-1]]
    # 表示上右下左四个邻接节点
    # 当某一个节点本身是岛屿，并且它的的上下左右四个相邻节点都是被访问过，或者是水的话，那么就岛屿加一
    # 只要是没有访问过的节点，就需要添加到队列中
    # 用来找某个节点的连通图，并且标记它们为已访问，这样可以把整个岛屿都标记了
    def bfs(i,j):
        queue.append((i,j))
        visited[0][0]=True
        while queue:
            # print(f"queue: {queue}")
            # 弹出队列里的首数据
            i,j=queue.popleft() 
            for k,p in enumerate(bac):
                temi=i+p[0]
                temj=j+p[1]
                # print(f"temi: {temi}")
                # print(f"temj: {temj}")
                if temi>=0 and temi<n and temj>=0 and temj<m:
                    # 满足边界条件
                    if not visited[temi][temj]:
                        if graph[temi][temj]==1:
                            visited[temi][temj]=True
                            queue.append((temi,temj))
            # print(f"isiso: {isiso}")
            # print(f"graph: {graph[i][j]}")
    def dfs(i,j):
        for k,p in enumerate(bac):
            temi=i+p[0]
            temj=j+p[1]
            # print(f"temi: {temi}")
            # print(f"temj: {temj}")
            if temi>=0 and temi<n and temj>=0 and temj<m:
                # 满足边界条件
                if not visited[temi][temj]:
                    if graph[temi][temj]==1:
                        visited[temi][temj]=True
                        dfs(temi,temj)
    # 这里需要遍历整个矩阵
    ans=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and not visited[i][j]:
                ans+=1
                # bfs(i,j)
                dfs(i,j)
    print(ans)
if __name__=="__main__":
    main()






