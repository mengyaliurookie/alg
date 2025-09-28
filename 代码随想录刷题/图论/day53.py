# 110. 字符串接龙
topic="""
题目描述
字典 strList 中从字符串 beginStr 和 endStr 的转换序列是一个按下述规格形成的序列： 



1. 序列中第一个字符串是 beginStr。

2. 序列中最后一个字符串是 endStr。 

3. 每次转换只能改变一个字符。 

4. 转换过程中的中间字符串必须是字典 strList 中的字符串，且strList里的每个字符串只用使用一次。 



给你两个字符串 beginStr 和 endStr 和一个字典 strList，找到从 beginStr 到 endStr 的最短转换序列中的字符串数目。如果不存在这样的转换序列，返回 0。

输入描述
第一行包含一个整数 N，表示字典 strList 中的字符串数量。 第二行包含两个字符串，用空格隔开，分别代表 beginStr 和 endStr。 后续 N 行，每行一个字符串，代表 strList 中的字符串。
输出描述
输出一个整数，代表从 beginStr 转换到 endStr 需要的最短转换序列中的字符串数量。如果不存在这样的转换序列，则输出 0。
输入示例
6
abc def
efc
dbc
ebc
dec
dfc
yhn
输出示例
4
提示信息
从 startStr 到 endStr，在 strList 中最短的路径为 abc -> dbc -> dec -> def，所以输出结果为 4，如图：

数据范围：

2 <= N <= 500
"""

import sys
from collections import Counter,deque
import math

def isok(a, b):
    """判断两个字符串是否只相差一个字符"""
    if len(a) != len(b):
        return False
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            if diff > 1:
                return False
    return diff == 1


def main():
    n=int(input())
    beginStr,endStr=input().strip().split()
    bag={}
    for _ in range(n):
        tstr=input().strip()
        bag[tstr]=0
    # =0表示还可以选
    # print(f"bag = {bag}")
    ans=math.inf
    def bfs():
        queue=deque()
        queue.append((beginStr,1))
        while queue:
            word,step=queue.popleft()
            if isok(word,endStr):
                return step+1
            for s,i in bag.items():
                if i==0 and isok(s,word):
                    queue.append((s,step+1))
                    bag[s]=1
        return -1
    ans=bfs()
    if ans==-1:
        print(0)
    else:
        print(ans)




# 106. 岛屿的周长
topic="""
106. 海岸线计算
题目描述
给定一个由 1（陆地）和 0（水）组成的矩阵，岛屿是被水包围，并且通过水平方向或垂直方向上相邻的陆地连接而成的。

你可以假设矩阵外均被水包围。在矩阵中恰好拥有一个岛屿，假设组成岛屿的陆地边长都为 1，请计算海岸线，即：岛屿的周长。岛屿内部没有水域。

输入描述
第一行包含两个整数 N, M，表示矩阵的行数和列数。之后 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。
输出描述
输出一个整数，表示岛屿的周长。
输入示例
5 5
0 0 0 0 0 
0 1 0 1 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
输出示例
14
提示信息
岛屿的周长为 14。
数据范围：
1 <= M, N <= 50。
"""

import sys
from collections import deque

# 思路是，遍历岛屿的时候，看看四周是不是0，如果是0，就把周长加1
# 不过要注意的是，因为会有靠边的情况，所以需要在矩阵的四周都加一圈0
def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    grid=[]
    for i in range(n+2):
        if i==0:
            grid.append([0]*(m+2))
        elif i==n+1:
            grid.append([0]*(m+2))
        else:
            grid.append([0]+list(map(int,sys.stdin.readline().strip().split()))+[0])
    n=n+2
    m=m+2
    visited=[[False]*m for _ in range(n)]
    direction=[[1,0],[0,1],[-1,0],[0,-1]]
    def dfs(i,j):
        # 因为一开始是保证i，j指向的一定是1，并且四周是1的才会递归，所以不需要判断是不是1了
        res=0
        if visited[i][j]==False:
            visited[i][j]=True
        for f in direction:
            nexti=i+f[0]
            nextj=j+f[1]
            if 0<=nexti<n and 0<=nextj<m:
                if grid[nexti][nextj]==0:
                    res+=1
                if grid[nexti][nextj]==1 and visited[nexti][nextj]==False:
                    res+=dfs(nexti,nextj)
        return res
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and visited[i][j]==False:
                ans=dfs(i,j)
    print(ans)          




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



