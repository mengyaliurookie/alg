# 100. 岛屿的最大面积
topic="""
100. 最大岛屿的面积
题目描述
给定一个由 1（陆地）和 0（水）组成的矩阵，计算岛屿的最大面积。岛屿面积的计算方式为组成岛屿的陆地的总数。岛屿由水平方向或垂直方向上相邻的陆地连接而成，并且四周都是水域。你可以假设矩阵外均被水包围。
输入描述
第一行包含两个整数 N, M，表示矩阵的行数和列数。后续 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。
输出描述
输出一个整数，表示岛屿的最大面积。如果不存在岛屿，则输出 0。
输入示例
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例
4
提示信息




样例输入中，岛屿的最大面积为 4。



数据范围：

1 <= M, N <= 50。
"""
# 感觉和岛屿计数的思路是一样的，只不过在标记岛屿的时候，需要记录一下岛屿的面积
import sys
from collections import deque

def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    iso=[]
    visited=[]
    for _ in range(n):
        iso.append(list(map(int,sys.stdin.readline().strip().split())))
        visited.append([False]*m)
    layer=[[1,0],[0,1],[-1,0],[0,-1]]
    def bfs(i,j):
        ans=0
        queue=deque()
        queue.append((i,j))
        visited[i][j]=True
        ans+=1
        while queue:
            k,l=queue.popleft()
            for f in layer:
                temi=k+f[0]
                temj=l+f[1]
                if 0<=temi<n and 0<=temj<m:
                    if iso[temi][temj]==1 and not visited[temi][temj]:
                        queue.append((temi,temj))
                        visited[temi][temj]=True
                        ans+=1
        return ans
    res=0
    for i in range(n):
        for j in range(m):
            if iso[i][j]==1 and not visited[i][j]:
                res=max(bfs(i,j),res)
    print(res)

import sys
from collections import deque

# 包括深度优先搜索和广度优先搜索
def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    iso=[]
    visited=[]
    for _ in range(n):
        iso.append(list(map(int,sys.stdin.readline().strip().split())))
        visited.append([False]*m)
    layer=[[1,0],[0,1],[-1,0],[0,-1]]
    def bfs(i,j):
        ans=0
        queue=deque()
        queue.append((i,j))
        visited[i][j]=True
        ans+=1
        while queue:
            k,l=queue.popleft()
            for f in layer:
                temi=k+f[0]
                temj=l+f[1]
                if 0<=temi<n and 0<=temj<m:
                    if iso[temi][temj]==1 and not visited[temi][temj]:
                        queue.append((temi,temj))
                        visited[temi][temj]=True
                        ans+=1
        return ans
    ans=0
    def dfs(i,j):
        # 深度优先搜索
        # ans=1
        for f in layer:
            temi=i+f[0]
            temj=j+f[1]
            if 0<=temi<n and 0<=temj<m:
                if iso[temi][temj]==1 and not visited[temi][temj]:
                    visited[temi][temj]=True
                    nonlocal ans
                    ans+=1
                    dfs(temi,temj)
                    # ans+=+1
    res=0
    for i in range(n):
        for j in range(m):
            if iso[i][j]==1 and not visited[i][j]:
                # res=max(bfs(i,j),res)
                visited[i][j]=True
                ans=1
                dfs(i,j)
                res=max(res,ans)
                # res=max(dfs(i,j),res)
    print(res)


# 101. 孤岛的总面积
topic="""
题目描述
给定一个由 1（陆地）和 0（水）组成的矩阵，岛屿指的是由水平或垂直方向上相邻的陆地单元格组成的区域，且完全被陆地单元格包围。孤岛是那些位于矩阵内部、所有单元格都不接触边缘的岛屿。



现在你需要计算所有孤岛的总面积，岛屿面积的计算方式为组成岛屿的陆地的总数。

输入描述
第一行包含两个整数 N, M，表示矩阵的行数和列数。之后 N 行，每行包含 M 个数字，数字为 1 或者 0。
输出描述
输出一个整数，表示所有孤岛的总面积，如果不存在孤岛，则输出 0。
输入示例
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例
1
提示信息

在矩阵中心部分的岛屿，因为没有任何一个单元格接触到矩阵边缘，所以该岛屿属于孤岛，总面积为 1。

数据范围：

1 <= M, N <= 50。
"""

# 本质上和上面的一个思路，只不过在过程中统计某个数据的方式不一样
# 不对，这里对孤岛的定义是不一样的
# 孤岛是那些位于矩阵内部、所有单元格都不接触边缘的岛屿。
# 需要加一个判断，就是如果岛屿不包括边界的话，就返回一个个数，包括的话就返回0

def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    iso=[]
    visited=[]
    for _ in range(n):
        iso.append(list(map(int,sys.stdin.readline().strip().split())))
        visited.append([False]*m)
    ans=0
    layer=[[1,0],[0,1],[-1,0],[0,-1]]
    # 广度优先搜索
    def bfs(i,j):
        res=1
        queue=deque()
        # 首节点加入队列
        queue.append((i,j))
        visited[i][j]=True
        isb=False
        if i in [0,n-1] or j in [0,m-1]:
            isb=True
        while queue:
            i,j=queue.popleft()
            for f in layer:
                temi=i+f[0]
                temj=j+f[1]
                if 0<=temi<n and 0<=temj<m:
                    if iso[temi][temj]==1 and not visited[temi][temj]:
                        if temi in [0,n-1] or temj in [0,m-1]:
                            isb=True
                        visited[temi][temj]=True
                        queue.append((temi,temj))
                        res+=1
        return 0 if isb else res
    for i in range(n):
        for j in range(m):
            if iso[i][j]==1 and not visited[i][j]:
                # print(f"i : {i} j : {j}")
                # print(bfs(i,j))
                # ans+=bfs(i,j)
                res=0
                dfs(i,j)
                print(f"i: {i} j:{j}")
                print(f"res: {res}")
                ans+=res
    print(ans)

# 还有一种思路是，先把挨着边的岛屿都标记成海洋，然后在遍历一遍，统计剩下的岛屿的面积
import sys
from collections import deque


def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    iso=[]
    visited=[]
    for _ in range(n):
        iso.append(list(map(int,sys.stdin.readline().strip().split())))
        visited.append([False]*m)
    ans=0
    layer=[[1,0],[0,1],[-1,0],[0,-1]]
    # 广度优先搜索
    def bfs(i,j):
        res=1
        queue=deque()
        # 首节点加入队列
        queue.append((i,j))
        visited[i][j]=True
        isb=False
        if i in [0,n-1] or j in [0,m-1]:
            isb=True
        while queue:
            i,j=queue.popleft()
            for f in layer:
                temi=i+f[0]
                temj=j+f[1]
                if 0<=temi<n and 0<=temj<m:
                    if iso[temi][temj]==1 and not visited[temi][temj]:
                        if temi in [0,n-1] or temj in [0,m-1]:
                            isb=True
                        visited[temi][temj]=True
                        queue.append((temi,temj))
                        res+=1
        return 0 if isb else res
    
    def dfs(i,j):
        # visited[i][j]=True
        iso[i][j]=0
        for f in layer:
            temi=i+f[0]
            temj=j+f[1]
            if 0<=temi<n and 0<=temj<m:
                if iso[temi][temj]==1 and not visited[temi][temj]:
                    iso[temi][temj]=0
                    # visited[temi][temj]=True
                    dfs(temi,temj)
    for i in range(m):
        if iso[0][i]==1:
            dfs(0,i)
        if iso[n-1][i]==1:
            dfs(n-1,i)
    for i in range(n):
        if iso[i][0]==1:
            dfs(i,0)
        if iso[i][m-1]==1:
            dfs(i,m-1)
    for i in range(n):
        for j in range(m):
            if iso[i][j]==1:
                # print(f"i : {i} j : {j}")
                # print(bfs(i,j))
                # ans+=bfs(i,j)
                ans+=1
    print(ans)


# 102. 沉没孤岛
topic="""
题目描述
给定一个由 1（陆地）和 0（水）组成的矩阵，岛屿指的是由水平或垂直方向上相邻的陆地单元格组成的区域，且完全被水域单元格包围。孤岛是那些位于矩阵内部、所有单元格都不接触边缘的岛屿。



现在你需要将所有孤岛“沉没”，即将孤岛中的所有陆地单元格（1）转变为水域单元格（0）。

输入描述
第一行包含两个整数 N, M，表示矩阵的行数和列数。

之后 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。

输出描述
输出将孤岛“沉没”之后的岛屿矩阵。 注意：每个元素后面都有一个空格
输入示例
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例
1 1 0 0 0
1 1 0 0 0
0 0 0 0 0
0 0 0 1 1
提示信息

将孤岛沉没。

数据范围：

1 <= M, N <= 50。
"""

# 可以先把挨着边的岛屿都标记为访问过，然后再把中间的岛屿都标记为0
import sys
from collections import deque

def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    iso=[]
    visited=[]
    for _ in range(n):
        iso.append(list(map(int,sys.stdin.readline().strip().split())))
        visited.append([False]*m)
    layer=[[1,0],[0,1],[-1,0],[0,-1]]

    def dfs(i,j):
        visited[i][j]=True
        for f in layer:
            temi=i+f[0]
            temj=j+f[1]
            if 0<=temi<n and 0<=temj<m:
                if iso[temi][temj]==1 and not visited[temi][temj]:
                    visited[temi][temj]=True
                    dfs(temi,temj)
    def bfs(i,j):
        queue=deque()
        queue.append((i,j))
        visited[i][j]=True
        while queue:
            i,j=queue.popleft()
            for f in layer:
                nexti=i+f[0]
                nextj=j+f[1]
                if 0<=nexti<n and 0<=nextj<m:
                    if iso[nexti][nextj]==1 and not visited[nexti][nextj]:
                        visited[nexti][nextj]=True
                        queue.append((nexti,nextj))
    for i in range(m):
        if iso[0][i]==1 and not visited[0][i]:
            # dfs(0,i)
            bfs(0,i)
        if iso[n-1][i]==1 and not visited[n-1][i]:
            # dfs(n-1,i)
            bfs(n-1,i)
    for j in range(n):
        if iso[j][0]==1 and not visited[j][0]:
            # dfs(j,0)
            bfs(j,0)
        if iso[j][m-1]==1 and not visited[j][m-1]:
            # dfs(j,m-1)
            bfs(j,m-1)
    for i in range(n):
        for j in range(m):
            if iso[i][j]==1 and not visited[i][j]:
                iso[i][j]=0
    for i in range(n):
        print(" ".join(list(map(str,iso[i]))))


