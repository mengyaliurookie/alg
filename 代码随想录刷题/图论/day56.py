
# prim算法精讲，最小生成树
topic="""
题目描述
在世界的某个区域，有一些分散的神秘岛屿，每个岛屿上都有一种珍稀的资源或者宝藏。国王打算在这些岛屿上建公路，方便运输。

不同岛屿之间，路途距离不同，国王希望你可以规划建公路的方案，如何可以以最短的总公路距离将 所有岛屿联通起来（注意：这是一个无向图）。 

给定一张地图，其中包括了所有的岛屿，以及它们之间的距离。以最小化公路建设长度，确保可以链接到所有岛屿。

输入描述
第一行包含两个整数V 和 E，V代表顶点数，E代表边数 。顶点编号是从1到V。例如：V=2，一个有两个顶点，分别是1和2。

接下来共有 E 行，每行三个整数 v1，v2 和 val，v1 和 v2 为边的起点和终点，val代表边的权值。

输出描述
输出联通所有岛屿的最小路径总距离
输入示例
7 11
1 2 1
1 3 1
1 5 2
2 6 1
2 4 2
2 3 2
3 4 1
4 5 1
5 6 2
5 7 1
6 7 1
输出示例
6
提示信息
数据范围：
2 <= V <= 10000;
1 <= E <= 100000;
0 <= val <= 10000;

如下图，可见将所有的顶点都访问一遍，总距离最低是6.
"""

from collections import deque
import math

# 从一个点出发，分别选可以达到的下一个节点，然后可以重复，当所有点都被访问过之后，就可以判断了
def main():
    p,e=map(int,input().strip().split())
    graph=[[0]*(p+1) for _ in range(p+1)]
    for _ in range(e):
        i,j,v=map(int,input().strip().split())
        graph[i][j]=v
    ans=math.inf
    # 最小生成树的话，那么其实可以采用并查集的方式来求解，因为是树的话就是没有环，这样可以使用并查集来判断有没有环。
    # 当要构成环的时候，就需要删除一个，这个删除不好整，那么可以通过递归来选一个，选两个，选三个这种
    # 但是这种时间复杂度就太大了，而且也不好实现


# 是会用到切分定理的
"""Cut Property（切分定理）
陈述：
把顶点集合划分为两部分 S 和 S_bar（即做一次“切分”）。在所有横跨该切分（端点一个在 S，另一个在 S_bar） 的边中，任取一条权值最小的边 e，则存在某棵最小生成树（MST）包含这条边 e。
（如果边权互不相等，则每个切分的最小横跨边必定属于所有的 MST。）
直观解释：
如果要把 S 和 S_bar 连通，至少要使用一条横跨切分的边。选取横跨切分的最小边显然不会比其他选择更差，因此把它加入构造最优解是安全的。
形式化证明（按“反证/交换”方法）：
设 e = (u,v) 是横跨切分 S / S_bar 的一条最小边，权为 w(e)。取任意一棵 MST，记为 T。
如果 e 已经在 T 中，那么结论成立。
否则，把 e 加入 T，得到连通图 T + e。由于 T 是树，加入一条边后必然在 T + e 中出现环。
这个环中必然存在至少一条其它边 f 也横跨该切分 S / S_bar。理由：e 的两个端点分别在 S 与 S_bar，沿环从 u 回到 v 必然有偶数次穿越切分，其中除 e 外至少还有一条横跨切分的边。
取环上这样的一条横跨切分的边 f，令其权为 w(f)。由于 e 是横跨切分的最小边，必有 w(e) <= w(f)。
将环上的 f 从 T + e 中删除，得到 T' = T + e - f。T' 仍然连通且边数为 V-1，所以是生成树。
总权比较：w(T') = w(T) + w(e) - w(f) <= w(T)。因 T 是 MST（权最小），所以必须有 w(T') = w(T)，即 T' 也是 MST。并且 T' 包含 e。
因此存在一棵 MST 包含 e，证毕。
补充（边权严格不同的情形）：
若横跨切分的最小边 e 的权严格小于环中任意其它横跨边 f 的权（即 w(e) < w(f)），则在上面的步骤 5-6 中会得到 w(T') < w(T)（除非 f 不存在），这与 T 为 MST 矛盾，因此在权严格不同时，任何 MST 都必须包含该最小横跨边 e。
推论与意义：
这就是 Kruskal 算法每次取最小边并尝试加入（若不构成环则加入）是正确的理由：所取的最小边是“安全边”（safe edge）。
这也是 Prim 算法每次从当前生成树向外取最小横切边的正确性基础。
当边权相等时，切分定理只保证“存在”某棵 MST 包含该最小边；不同的 MST 之间可能在相等权的边处做不同选择。
简单例子（直观回顾）：
假设某切分横跨边的权集合为 {3,5,7}，最小是 3。任取一棵 MST 若不包含权为 3 的那条边，把它加入会在环上找到权 >= 3 的横跨边 f，交换后权不增，从而仍是 MST。因此包含权 3 的边是安全的。
结束语：
切分定理是 MST 正确性证明的核心工具。它把“局部最优选择”（在某个切分上取最小横跨边）与“全局最优”（MST）联系起来，直接说明了为什么 Kruskal/Prim 的贪心选择是安全且最终能得到最优解的。"""
# 按照我的理解来的话是，两个切分，他们之间的最小边，假设某个最小生成树不包括这个最近小边的话，
# 然后把这个边加到最小生成树中，就可以构成一个环，而且在这两个切分之间是存在两条路径的，因为是最小的所以可以替换
"""
——————
最小生成树（MST）笔记 —— 思路与证明整理
——————

一、问题描述（目标）

给定一个无向带权连通图（V 个顶点，E 条边）。

要选出若干条边，使得：

图连通（所有顶点互相可达），

边数最少（生成树必须是 V-1 条），

总权和最小。

目标：求最小生成树的权值和（或返回所选的边集）。

二、常见的错误思路（你的原始 DFS）

你的 DFS 思路：从某一点出发，依次走遍所有未访问点，直到 path 为空（所有点被访问），记录路径长度，取最小。

这在本质上是枚举“覆盖所有点的一条链”（Hamilton 路径 / TSP），而不是枚举生成树。

MST 允许分叉（树结构），不必是一条链。

TSP/Hamilton 路径通常要更长，且是 NP 难（穷举复杂度指数级）。

结论：用“走一条线覆盖所有点”的 DFS，不会得到 MST（而是求 TSP），效率也非常低。

三、正确思路（贪心 + 切分定理）

常用高效算法：Kruskal（按边排序 + 并查集）或 Prim（从任一点出发，贪心扩展最小跨界边）。复杂度为多项式。

正确性的核心：切分定理（Cut Property）——每次在某个切分上取横跨切分的最小边是“安全边”，可以加入到某棵 MST 中。

四、切分定理（Cut Property） —— 纯文本证明（交换法）

陈述（简洁）：

任取顶点集的任意划分（S, S_bar），在所有横跨 S 与 S_bar 的边中，取最小权的边 e（在这个横跨边集合里最小）。则存在某棵 MST 包含 e。

证明（反证/交换）：
a. 取任意一棵 MST，记为 T。
b. 若 e 已在 T 中，则结论成立。
c. 若 e 不在 T，把 e 加入 T（T 是树，加一边会形成一个环）。
d. 在这个环上，必然存在另一条横跨同一切分的边 f（因为 e 的两个端点分别在 S 和 S_bar，沿环回到起点必然还有其它跨界边）。
e. 由于 e 是横跨该切分的最小边，所以 w(e) <= w(f)。
f. 从 T + e 中删除 f，得到 T' = T + e − f。T' 仍然连通并且有 V-1 条边（仍是树）。其权和 w(T') = w(T) + w(e) − w(f) <= w(T)。
g. 因为 T 是 MST（最小权），所以 w(T') = w(T)，即 T' 也是 MST，且包含 e。证毕。

备注：若横跨边权严格不同，则更强 —— 那个最小横跨边必然出现在所有 MST 中。

五、环上替换安全性的直观与为何不破坏全局连通

加边 e 于树 T：

T 是树（所有点连通且无环）。加入 e = (u,v) 时，树中 u 到 v 原有唯一路径 P，加入 e 就把 P 与 e 组成一个环 C。

删除环上的某条边 f（f 可能在 P 上）：

环的性质：去掉环的任意一条边，环上所有点仍连通（因为环的其余部分连通）。

原来不在环上的点，其通往环的路径至少通过环上的某点；只要环上的点仍连通（删除 f 后仍保持），环外点与环的连通性不受影响。

因此删除 f 后，整个图仍连通且边数回到 V−1（仍是生成树）。

权重：因为 w(e) <= w(f)，所以新树的权和不大于原树。因此替换合法而且安全。
"""

from collections import deque
import math

# 从一个点出发，分别选可以达到的下一个节点，然后可以重复，当所有点都被访问过之后，就可以判断了
def main():
    p,e=map(int,input().strip().split())
    graph=[[] for _ in range(p+1)]
    for _ in range(e):
        i,j,v=map(int,input().strip().split())
        graph[i].append((j,v))
        graph[j].append((i,v))
    ans=math.inf
    # print(graph)
    # [[], [(2, 1), (3, 1), (5, 2)], [(6, 1), (4, 2), (3, 2)], [(4, 1)], [(5, 1)], [(6, 2), (7, 1)], [(7, 1)], []]
    # 需要定义一个数组来表示未选节点到已选节点的最小距离
    # 定义一个集合来存储已经选的节点
    # 定义一个集合来存储已经选的边
    # 定义一个集合来存储未选的点
    minDist=[10001 for _ in range(p+1)]
    left=set()
    left.add(1)
    cur=1
    # right=(i for i in ramge(2,p+1))
    edges=set()
    # 共需要选n-1条边，所以外层需要循环n-1次就可以
    for _ in range(p):
        # print(f"cur: {cur}")
        # 开始选的是1节点
        # 需要把当前节点连接的节点更新一下，然后看看哪个最小，需要把它加到left中，作为下一个选择的节点
        choices=graph[cur] 
        for point,leng in choices: 
            if point not in left and leng<minDist[point]:
                minDist[point]=leng
        # 
        mintem=math.inf
        for i in range(1,p+1):
            if i not in left and mintem>minDist[i]:
                cur=i
                mintem=minDist[i]
        left.add(cur)
        
    # print(minDist)
    ans=0
    for i in range(2,p+1):
        ans+=minDist[i]
    print(ans)


# kruskal算法精讲
from collections import deque
import math

father=[]

# 并查集的实现
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


# 从一个点出发，分别选可以达到的下一个节点，然后可以重复，当所有点都被访问过之后，就可以判断了
def main():
    p,e=map(int,input().strip().split())
    graph=[list(map(int,input().strip().split())) for _ in range(e)]
    graph.sort(key=lambda x:x[-1])
    ans=0
    global father
    father=[i for i in range(p+1)]
    for i,j,k in graph:
        if not issame(i,j):
            ans+=k
            union(i,j)
        
    print(ans)



# 拓扑排序精讲
def main():
    # 拓扑排序，找到入度为0的点，然后加入到集合中，然后从图上把它删除
    # 找入度为0的点，用邻接矩阵的话，就是判断某一列都是0的话，就是入度为0
    # 从图上删除的话，就是把这一行和这一列都置为0
    # 还需要判断有没有环，如果还有节点，但是不存在入度为0的点了，就证明有环了
    # 但是这么写复杂度有点高。
    # 如果直接用来存储每个节点的入度的话会更好一点，再删除的时候，遍历一遍节点然后
    n,m=map(int,input().strip().split())
    graph=[[0]*(n) for _ in range(n)]
    degree=[0]*(n)
    for _ in range(m):
        i,j=map(int,input().strip().split())
        graph[i][j]=1
        degree[j]+=1
    ans=[]
    has=set()
    
    for _ in range(n):
        # 总体上需要打印n个点，所以需要遍历n遍
        # 查找degree中为0的点
        hashu=True
        for i,d in enumerate(degree):
            if i not in has and d==0:
                ans.append(i)
                has.add(i)
                hashu=False
                break
        if hashu:
            # 说明没有为0的节点了
            print(-1)
            break
        # 删除节点然后更新入度
        for j in range(n):
            if graph[i][j]==1:
                degree[j]-=1
    if not hashu:
        print(" ".join(list(map(str,ans))))
        





