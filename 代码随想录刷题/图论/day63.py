# Bellman_ford 算法精讲
topic="""
94. 城市间货物运输 I
题目描述
某国为促进城市间经济交流，决定对货物运输提供补贴。共有 n 个编号为 1 到 n 的城市，通过道路网络连接，网络中的道路仅允许从某个城市单向通行到另一个城市，不能反向通行。



网络中的道路都有各自的运输成本和政府补贴，道路的权值计算方式为：运输成本 - 政府补贴。权值为正表示扣除了政府补贴后运输货物仍需支付的费用；权值为负则表示政府的补贴超过了支出的运输成本，实际表现为运输过程中还能赚取一定的收益。



请找出从城市 1 到城市 n 的所有可能路径中，综合政府补贴后的最低运输成本。如果最低运输成本是一个负数，它表示在遵循最优路径的情况下，运输过程中反而能够实现盈利。



城市 1 到城市 n 之间可能会出现没有路径的情况，同时保证道路网络中不存在任何负权回路。

输入描述
第一行包含两个正整数，第一个正整数 n 表示该国一共有 n 个城市，第二个整数 m 表示这些城市中共有 m 条道路。 

接下来为 m 行，每行包括三个整数，s、t 和 v，表示 s 号城市运输货物到达 t 号城市，道路权值为 v （单向图）。

输出描述
如果能够从城市 1 到连通到城市 n， 请输出一个整数，表示运输成本。如果该整数是负数，则表示实现了盈利。如果从城市 1 没有路径可达城市 n，请输出 "unconnected"。
输入示例
6 7
5 6 -2
1 2 1
5 3 1
2 5 2
2 4 -3
4 6 4
1 3 5
输出示例
1
提示信息


示例中最佳路径是从 1 -> 2 -> 5 -> 6，路上的权值分别为 1 2 -2，最终的最低运输成本为 1 + 2 + (-2) = 1。



示例 2：

4 2
1 2 -1
3 4 -1

在此示例中，无法找到一条路径从 1 通往 4，所以此时应该输出 "unconnected"。



数据范围：

1 <= n <= 1000；
1 <= m <= 10000;

-100 <= v <= 100;
"""
import math

def main():
    n,m=map(int,input().strip().split())
    graph=[]
    for _ in range(m):
        i,j,v=map(int,input().strip().split())
        graph.append((i,j,v))
    # 邻接表存储图
    mindist=[math.inf]*(n+1)
    # mindist表示从源点出发可以到大的最短路径值
    # 利用bellman算法求解
    # 因为有n个节点，最短路径的话，如果存在,使用n-1轮就可以达到
    mindist[1]=0
    for i in range(1,n):
        updated = False
        # 每一轮表示经过i条边可以达到的最短距离
        for j,k,v in graph:
            # 遍历所有边,如果当前节点可以从源点出发到达，并且经过当前节点到达其他节点是从源点出发的更短的路径，那么就更新其他节点
            if mindist[j]!=math.inf and mindist[k]>mindist[j]+v:
                mindist[k]=mindist[j]+v
                updated = True
        if not updated:
            break
    if mindist[n]==math.inf:
        print("unconnected")
    else:
        print(mindist[n])

# 队列优化版本的bellman_ford算法，
# 因为bellman_ford算法是每次遍历所有的边，代表着从源点出发经过多少条边可以到达边的终点的位置的最短路径
# 而队列优化版本的bellman_ford算法，是每次遍历所有的边，代表着从源点出发经过多少条边可以到达边的终点的位置的最短路径
# 但是只有当边的终点的最短路径长度发生了变化，才会将边的终点加入到队列中
import math
from collections import deque
def main():
    n,m=map(int,input().strip().split())
    edges=[[] for _ in range(n+1)]
    for _ in range(m):
        i,j,v=map(int,input().strip().split())
        edges[i].append((j,v))
    mindist=[math.inf]*(n+1)
    # 表示从源点出发到达每个点的最短路径长度
    # 初始化从源点到达源点的最短路径为0
    mindist[1]=0
    # 因为到达n点的话，最短路径最多可以把每个顶点都经历一遍，这样就最多有n-1条边。如果还可以多次经过同一顶点的话，那么必然有环，此时可以选择不走环就可以了。
    # 每次遍历所有的边，代表着从源点出发经过多少条边可以到达边的终点的位置的最短路径
    queue=deque()
    queue.append(1)
    while queue:
        i=queue.popleft()
        for j,k in edges[i]:
            if  mindist[j]>mindist[i]+k:
                mindist[j]=mindist[i]+k
                queue.append(j)
    if mindist[n]==math.inf:
        print("unconnected")
    else:
        print(mindist[n])
    
