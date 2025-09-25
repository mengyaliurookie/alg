# 103. 水流问题
topic="""
题目描述
现有一个 N × M 的矩阵，每个单元格包含一个数值，这个数值代表该位置的相对高度。矩阵的左边界和上边界被认为是第一组边界，而矩阵的右边界和下边界被视为第二组边界。



矩阵模拟了一个地形，当雨水落在上面时，水会根据地形的倾斜向低处流动，但只能从较高或等高的地点流向较低或等高并且相邻（上下左右方向）的地点。我们的目标是确定那些单元格，从这些单元格出发的水可以达到第一组边界和第二组边界。

输入描述
第一行包含两个整数 N 和 M，分别表示矩阵的行数和列数。 

后续 N 行，每行包含 M 个整数，表示矩阵中的每个单元格的高度。

输出描述
输出共有多行，每行输出两个整数，用一个空格隔开，表示可达第一组边界和第二组边界的单元格的坐标，输出顺序任意。
输入示例
5 5
1 3 1 2 4
1 2 1 3 2
2 4 7 2 1
4 5 6 1 1
1 4 1 2 1
输出示例
0 4
1 3
2 2
3 0
3 1
3 2
4 0
4 1
提示信息

图中的蓝色方块上的雨水既能流向第一组边界，也能流向第二组边界。所以最终答案为所有蓝色方块的坐标。 

数据范围：

1 <= M, N <= 100。
"""

import sys
from collections import deque

# 这完全是暴力的方式求解，有10个用例是可以ac的，但是第11个用例超时了
def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    grid=[]
    
    for _ in range(n):
        grid.append(list(map(int,sys.stdin.readline().strip().split())))
        
    # 上下左右四条路，可以走一直走到边界
    layer=[[1,0],[0,1],[-1,0],[0,-1]]
    # 可以用一个矩阵来保存各个点是否可以到达边界
    # 这个矩阵可以存储各种状态，0表示不可以打到边界，1表示可以到达第一组边界，2表示可以到达第二组边界，3表示还不清楚
    
    def dfs(i,j):
        visited[i][j]=True
        if i==0 or j==0:
            touch[0]=True
        if i==n-1 or j==m-1:
            touch[1]=True
        for f in layer:
            nexti=i+f[0]
            nextj=j+f[1]
            if 0<=nexti<n and 0<=nextj<m:
                # 表示在范围内
                if visited[nexti][nextj]==False and grid[i][j]>=grid[nexti][nextj]:
                    if nexti==0 or nextj==0:
                        touch[0]=True
                    if nexti==n-1 or nextj==m-1:
                        touch[1]=True
                    visited[nexti][nextj]=True
                    dfs(nexti,nextj)
    ans=[]
    for i in range(n):
        for j in range(m):
            visited=[[False]*m for _ in range(n)]
            touch=[False,False]
            dfs(i,j)
            if all(touch):
                ans.append((i,j))
    # print(ans)
    for a in ans:
        print(" ".join(list(map(str,a))))


# 加了一个在递归的时候的提前的判断，如果当前已经有路径可以达到第一组和第二组边界，那么就可以直接返回了
def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    grid=[]
    
    for _ in range(n):
        grid.append(list(map(int,sys.stdin.readline().strip().split())))
        
    # 上下左右四条路，可以走一直走到边界
    layer=[[1,0],[0,1],[-1,0],[0,-1]]
    # 可以用一个矩阵来保存各个点是否可以到达边界
    # 这个矩阵可以存储各种状态，0表示不可以打到边界，1表示可以到达第一组边界，2表示可以到达第二组边界，3表示还不清楚
    
    def dfs(i,j):
        visited[i][j]=True
        if i==0 or j==0:
            touch[0]=True
        if i==n-1 or j==m-1:
            touch[1]=True
        if all(touch):
            return
        for f in layer:
            nexti=i+f[0]
            nextj=j+f[1]
            if 0<=nexti<n and 0<=nextj<m:
                # 表示在范围内
                if visited[nexti][nextj]==False and grid[i][j]>=grid[nexti][nextj]:
                    if nexti==0 or nextj==0:
                        touch[0]=True
                    if nexti==n-1 or nextj==m-1:
                        touch[1]=True
                    visited[nexti][nextj]=True
                    dfs(nexti,nextj)
    ans=[]
    for i in range(n):
        for j in range(m):
            visited=[[False]*m for _ in range(n)]
            touch=[False,False]
            dfs(i,j)
            if all(touch):
                ans.append((i,j))
    # print(ans)
    for a in ans:
        print(" ".join(list(map(str,a))))

# 加了一些提前返回的节点，但是
def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    grid=[]
    isok=[]
    for _ in range(n):
        grid.append(list(map(int,sys.stdin.readline().strip().split())))
        isok.append([4]*m)
        
    # 上下左右四条路，可以走一直走到边界
    layer=[[1,0],[0,1],[-1,0],[0,-1]]
    # 可以用一个矩阵来保存各个点是否可以到达边界
    # 这个矩阵可以存储各种状态，0表示不可以打到边界，1表示可以到达第一组边界和2表示可以到达第二组边界，3表示可以到达两组边界，4表示还不清楚
    
    def dfs(i,j):
        if isok[i][j]==3:
            touch[0]=True
            touch[1]=True
            return
        elif isok[i][j]==1:
            touch[0]=True
            return
        elif isok[i][j]==2:
            touch[1]=True
            return
        elif isok[i][j]==0:
            return
        visited[i][j]=True
        if i==0 or j==0:
            touch[0]=True
        if i==n-1 or j==m-1:
            touch[1]=True
        if all(touch):
            return
        for f in layer:
            nexti=i+f[0]
            nextj=j+f[1]
            if 0<=nexti<n and 0<=nextj<m:
                # 表示在范围内
                if visited[nexti][nextj]==False and grid[i][j]>=grid[nexti][nextj]:
                    if nexti==0 or nextj==0:
                        touch[0]=True
                    if nexti==n-1 or nextj==m-1:
                        touch[1]=True
                    visited[nexti][nextj]=True
                    dfs(nexti,nextj)
    ans=[]
    for i in range(n):
        for j in range(m):
            visited=[[False]*m for _ in range(n)]
            touch=[False,False]
            dfs(i,j)
            if all(touch):
                isok[i][j]=3
                ans.append((i,j))
            elif touch[0]==True:
                isok[i][j]=1
            elif touch[1]==True:
                isok[i][j]=2
            else:
                isok[i][j]=0
    # print(ans)
    for a in ans:
        print(" ".join(list(map(str,a))))

# 换另一种思路，就是分别从第一组和第二组的边界开始，向内部搜索，
# 如果搜索到的点的高度大于等于当前点的高度，那么就可以到达当前点
# 最后如果当前点可以到达第一组和第二组的边界，那么就可以加入到答案中

def main():
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # 0 = 不可达任一边界, 1 = 上/左, 2 = 下/右, 3 = 两边, 4 = 未知
    
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    def dfs(i, j,side):
        if visited[i][j]==True:
            return
        visited[i][j]=True
        side.add((i,j))
        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] >= grid[i][j]:
                dfs(ni, nj,side)
    # 从第一组边界出发
    visited = [[False]*m for _ in range(n)]
    left=set()
    for i in range(m):
        dfs(0,i,left)
    for j in range(n):
        dfs(j,0,left) 
    
    # 从第二组边界出发
    visited = [[False]*m for _ in range(n)]
    right=set()
    for i in range(m):
        dfs(n-1,i,right)
    for j in range(n):
        dfs(j,m-1,right) 

    ans = left & right
    for x, y in ans:
        print(x, y)


# 104.建造最大岛屿
topic="""
题目描述
给定一个由 1（陆地）和 0（水）组成的矩阵，你最多可以将矩阵中的一格水变为一块陆地，在执行了此操作之后，矩阵中最大的岛屿面积是多少。



岛屿面积的计算方式为组成岛屿的陆地的总数。岛屿是被水包围，并且通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设矩阵外均被水包围。

输入描述
第一行包含两个整数 N, M，表示矩阵的行数和列数。之后 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。
输出描述
输出一个整数，表示最大的岛屿面积。
输入示例
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例
6
提示信息

对于上面的案例，有两个位置可将 0 变成 1，使得岛屿的面积最大，即 6。


数据范围：

1 <= M, N <= 50。
"""
# 可以采用通过把每个0都尝试变成一之后，去利用dfs搜索，
import sys
from collections import deque
token=0
def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    grid=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
    visited=[[-1]*m for _ in range(n)]
    # visited中用小于i+j表示当前搜索还没有被访问过，用等于i+j表示已经被当前次访问过
    direc=[[1,0],[0,1],[-1,0],[0,-1]]
    def dfs(ii,jj):
        nonlocal res
        if visited[ii][jj]<token:
            res+=1
            visited[ii][jj]=token
        for f in direc:
            nexti=ii+f[0]
            nextj=jj+f[1]
            if 0<=nexti<n and 0<=nextj<m:
                # 满足范围
                if grid[nexti][nextj]==1 and visited[nexti][nextj]<token:
                    res+=1
                    visited[nexti][nextj]=token
                    dfs(nexti,nextj)
    ans=0
    for i in range(n):
        for j in range(m):
            global token
            token+=1
            if grid[i][j]==0:
                res=0
                grid[i][j]=1
                dfs(i,j)
                grid[i][j]=0
                # print(f"i= {i} j= {j}")
                # print(f"res= {res}")
                ans=max(ans,res)
            else:
                res=0
                dfs(i,j)
                # print(f"i= {i} j= {j}")
                # print(f"res= {res}")
                ans=max(ans,res)
    print(ans)


# 还有另外一种思路就是，先把所有岛屿的面积都计算出来，
# 然后遍历每个0，看它的上下左右是否有岛屿，如果有，就把它的面积加上去，
# 最后取所有0的面积的最大值即可
import sys
from collections import deque

token=0

def main():
    n,m=map(int,sys.stdin.readline().strip().split())
    grid=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
    visited=[[-1]*m for _ in range(n)]
    # visited中用小于i+j表示当前搜索还没有被访问过，用等于i+j表示已经被当前次访问过
    direc=[[1,0],[0,1],[-1,0],[0,-1]]
    
    visited=[[False]*m for _ in range(n)]
    def dfs(i,j,token):
        res=0
        if visited[i][j]==False:
            res+=1
            visited[i][j]=True
            isonum[i][j]=token
        for f in direc:
            nexti=i+f[0]
            nextj=j+f[1]
            if 0<=nexti<n and 0<=nextj<m:
                if grid[nexti][nextj]==1 and visited[nexti][nextj]==False:
                    res+=dfs(nexti,nextj,token)
        return res
    ans=0
    # 用一个同样的矩阵来记录岛屿编号
    isonum=[[0]*m for _ in range(n)]
    token=0
    dic={}
    # 先遍历一遍所有岛屿，并且记录下编号和面积
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and visited[i][j]==False:
                token+=1
                res=dfs(i,j,token)
                dic[token]=res
                # print(f"i= {i} j= {j}")
                # print(f"res= {res}")

    # 在遍历一遍海洋，看看海洋四周连接的岛屿的面积
    ans=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                res=1
                tem=set()
                for f in direc:
                    nexti=i+f[0]
                    nextj=j+f[1]
                    if 0<=nexti<n and 0<=nextj<m:
                        # 查看一下上下左右所属的岛屿
                        if isonum[nexti][nextj]>0:
                            tem.add(isonum[nexti][nextj])
                for t in tem:
                    res+=dic[t]
                ans=max(ans,res)
            else:
                ans=max(ans,dic[isonum[i][j]])

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



