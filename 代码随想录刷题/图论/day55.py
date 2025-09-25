# 105.有向图的完全联通
topic="""
题目描述
给定一个有向图，包含 N 个节点，节点编号分别为 1，2，...，N。现从 1 号节点开始，如果可以从 1 号节点的边可以到达任何节点，则输出 1，否则输出 -1。
输入描述
第一行包含两个正整数，表示节点数量 N 和边的数量 K。 后续 K 行，每行两个正整数 s 和 t，表示从 s 节点有一条边单向连接到 t 节点。
输出描述
如果可以从 1 号节点的边可以到达任何节点，则输出 1，否则输出 -1。
输入示例
4 4
1 2
2 1
1 3
2 4
输出示例
1
提示信息

从 1 号节点可以到达任意节点，输出 1。

数据范围：

1 <= N <= 100；
1 <= K <= 2000。
"""

import sys
from collections import deque

def main():
    # 读取并存储图
    n,k=map(int,input().strip().split())
    grid=[[0]*(n+1) for _ in range(n+1)]
    visited=[False]*(n+1)
    for i in range(k):
        j,m=map(int,input().strip().split())
        grid[j][m]=1
    # print(f"grid= {grid}")
    def bfs():
        queue=deque()
        # 从1节点开始
        queue.append(1)
        visited[1]=True
        while queue:
            point=queue.popleft()
            for i,v in enumerate(grid[point]):
                if v==1 and visited[i]==False:
                    queue.append(i)
                    visited[i]=True
    bfs()
    # print(f"visited= {visited}")
    if all(visited[1:]):
        print(1)
    else:
        print(-1) 


# 并查集理论基础
topic="""
背景
首先要知道并查集可以解决什么问题呢？

并查集常用来解决连通性问题。

大白话就是当我们需要判断两个元素是否在同一个集合里的时候，我们就要想到用并查集。

并查集主要有两个功能：

将两个元素添加到一个集合中。
判断两个元素在不在同一个集合
"""

# 并查集的代码模板
n=1024
# 这里包括了初始化，使用每个节点作为根
father=[i for i in range(n)]

def find(x):
    if x!=father[x]:
        father[x]=find(father[x])
    return father[x]

def isSame(x,y):
    return find(x)==find(y)

# 将x->y 这条边加入并查集
def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        father[x]=y

# 107. 寻找存在的路径
topic="""
题目描述
给定一个包含 n 个节点的无向图中，节点编号从 1 到 n （含 1 和 n ）。



你的任务是判断是否有一条从节点 source 出发到节点 destination 的路径存在。

输入描述
第一行包含两个正整数 N 和 M，N 代表节点的个数，M 代表边的个数。 

后续 M 行，每行两个正整数 s 和 t，代表从节点 s 与节点 t 之间有一条边。 

最后一行包含两个正整数，代表起始节点 source 和目标节点 destination。

输出描述
输出一个整数，代表是否存在从节点 source 到节点 destination 的路径。如果存在，输出 1；否则，输出 0。
输入示例
5 4
1 2
1 3
2 4
3 4
1 4
输出示例
1
提示信息




数据范围：

1 <= M, N <= 100。


"""
import sys

def find(u):
    if u!=father[u]:
        father[u]=find(father[u])
    return father[u]

def issame(u,v):
    u=find(u)
    v=find(v)
    return u==v

def union(u,v):
    u=find(u)
    v=find(v)
    if u!=v:
        father[v]=u
father=[]
def main():
    n,m=map(int,input().strip().split())
    # 初始化并查集
    global father
    father=[i for i in range(n+1)]
    for i in range(m):
        k,l=map(int,input().strip().split())
        union(k,l)
    k,l=map(int,input().strip().split())
    if issame(k,l):
        print(1)
    else:
        print(0)


if __name__=="__main__":
    main()