
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

# 108. 冗余连接
topic="""
题目描述
有一个图，它是一棵树，他是拥有 n 个节点（节点编号1到n）和 n - 1 条边的连通无环无向图，例如如图：





现在在这棵树上的基础上，添加一条边（依然是n个节点，但有n条边），使这个图变成了有环图，如图：





先请你找出冗余边，删除后，使该图可以重新变成一棵树。

输入描述
第一行包含一个整数 N，表示图的节点个数和边的个数。

后续 N 行，每行包含两个整数 s 和 t，表示图中 s 和 t 之间有一条边。

输出描述
输出一条可以删除的边。如果有多个答案，请删除标准输入中最后出现的那条边。
输入示例
3
1 2
2 3
1 3
输出示例
1 3
提示信息




图中的 1 2，2 3，1 3 等三条边在删除后都能使原图变为一棵合法的树。但是 1 3 由于是标准输出里最后出现的那条边，所以输出结果为 1 3



数据范围：

1 <= N <= 1000.
"""
import sys

father=[]

def find(u):
    if father[u]!=u:
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
        father[u]=v

def main():
    n=int(input().strip())
    # 如何能构成一个环呢，就是当加入的边数等于点数的时候，就出现环了
    # 在并查集中，当一个集合中的新加入的两个点都已经存在在此集合中的时候，那么就说明出现了环
    # 并查集的初始化
    global father
    father=[i for i in range(n+1)]
    for _ in range(n):
        i,j=map(int,input().strip().split())
        if issame(i,j):
            print(i,j)
        else:
            union(i,j)


# 109. 冗余连接II
topic="""
题目描述
有一种有向树,该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。有向树拥有 n 个节点和 n - 1 条边。如图： 





现在有一个有向图，有向图是在有向树中的两个没有直接链接的节点中间添加一条有向边。如图：




输入一个有向图，该图由一个有着 n 个节点(节点编号 从 1 到 n)，n 条边，请返回一条可以删除的边，使得删除该条边之后该有向图可以被当作一颗有向树。

输入描述
第一行输入一个整数 N，表示有向图中节点和边的个数。 

后续 N 行，每行输入两个整数 s 和 t，代表这是 s 节点连接并指向 t 节点的单向边

输出描述
输出一条可以删除的边，若有多条边可以删除，请输出标准输入中最后出现的一条边。
输入示例
3
1 2
1 3
2 3
输出示例
2 3
提示信息

在删除 2 3 后有向图可以变为一棵合法的有向树，所以输出 2 3

数据范围：

1 <= N <= 1000.
"""

father=[]

def find(u):
    if father[u]!=u:
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

def main():
    n=int(input().strip())
    # 如何能构成一个有向树呢，就是必须每个点只有一个入一个出，或者只有出，不能存在有两个入的情况，怎么表示入和出的呢
    # 也得是构成环的时候删除，但是删除哪个呢，可能需要记录一下指向
    # 出度是第一列
    # 入度是第二列
    # 因为只有一个父节点或者没有，所以入度必然小于等于1
    # 而只有一个入度的意思就是在构造的过程中，当u!=find(u)的时候，说明已经有一个
    # 又因为要构成一棵树，所以不能有环在
    # 并查集的初始化
    global father
    father=[i for i in range(n+1)]
    edges=[]
    # 这是处理入度为二的
    hastodel=[]
    for _ in range(n):
        i,j=map(int,input().strip().split())
        edges.append([i,j])
        # 如果没有被改变过
        if j==find(j):
            # 还需要判断一下有没有环
            union(i,j)
        else:
            # 就需要弹出一下
            oldi=father[j]
            hastodel.append([i,j])
            hastodel.append([oldi,j])             
    # 最后再把矛盾的加入
    # print(hastodel)
    # 如果构成环，那么必须删除环中的那个
    hashu=False
    for i,j in hastodel:
        if issame(i,j):
            print(i,j)
            hashu=True
            break
        else:
            union(i,j)
    # print(edges)
    if hastodel:
        if not hashu:
            print(hastodel[-1][0],hastodel[-1][1])
    else:
        # 否则就是直接形成一个环了
        father=[i for i in range(n+1)]
        for i,j in edges:
            if issame(i,j):
                print(i,j)
                break
            else:
                union(i,j)
    # print(father)

