import math
# bellman-ford算法，带负权回路的判断
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
    updated = False
    # 每一轮表示经过i条边可以达到的最短距离
    for j,k,v in graph:
        # 遍历所有边,如果当前节点可以从源点出发到达，并且经过当前节点到达其他节点是从源点出发的更短的路径，那么就更新其他节点
        if mindist[j]!=math.inf and mindist[k]>mindist[j]+v:
            mindist[k]=mindist[j]+v
            updated = True
    if updated:
        print("circle")
        return
    if mindist[n]==math.inf:
        print("unconnected")
    else:
        print(mindist[n])

        
# 队列优化版本的bellman_ford算法，带负权回路的判断
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
    inqueue=[False]*(n+1)
    count=[0]*(n+1)
    inqueue[1]=True
    count[1]+=1
    while queue:
        i=queue.popleft()
        inqueue[i]=False
        for j,k in edges[i]:
            if mindist[j]>mindist[i]+k:
                mindist[j]=mindist[i]+k
                if not inqueue[j]:
                    queue.append(j)
                    count[j]+=1
                    inqueue[j]=True
                    if count[j] >= n:  # 注意：是 >= n，不是 == n
                        print("circle")
                        return

    if mindist[n]==math.inf:
        print("unconnected")
    else:
        print(mindist[n])
    



if __name__=="__main__":
    main()




