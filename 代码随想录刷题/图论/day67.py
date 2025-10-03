# A * 算法精讲 （A star算法）
topic="""
127. 骑士的攻击
题目描述
在象棋中，马和象的移动规则分别是“马走日”和“象走田”。现给定骑士的起始坐标和目标坐标，要求根据骑士的移动规则，计算从起点到达目标点所需的最短步数。



棋盘大小 1000 x 1000（棋盘的 x 和 y 坐标均在 [1, 1000] 区间内，包含边界）

输入描述
第一行包含一个整数 n，表示测试用例的数量，1 <= n <= 100。

接下来的 n 行，每行包含四个整数 a1, a2, b1, b2，分别表示骑士的起始位置 (a1, a2) 和目标位置 (b1, b2)。

输出描述
输出共 n 行，每行输出一个整数，表示骑士从起点到目标点的最短路径长度。
输入示例
6
5 2 5 4
1 1 2 2
1 1 8 8
1 1 8 7
2 1 3 3
4 6 4 6
输出示例
2
4
6
5
1
0
提示信息
骑士移动规则如图，红色是起始位置，黄色是骑士可以走的地方。
"""
# 利用广度搜索算法求解，时间会超时
from collections import deque
def main():
    global graph
    n=int(input())
    examples=[list(map(int,input().strip().split())) for _ in range(n)]
    for x1,y1,x2,y2 in examples:
        bfs(x1,y1,x2,y2)
        print(graph[x2][y2])


graph=[]
def bfs(x1,y1,x2,y2):
    global graph
    graph=[[0]*1001 for _ in range(1001)]
    rang=[[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1]]
    queue=deque()
    queue.append((x1,y1))
    # graph[x1][y1]=1
    while queue:
        s1,s2=queue.popleft()
        if s1==x2 and s2==y2:
            break
        for i,j in rang:
            nexti=s1+i
            nextj=s2+j
            if 1<=nexti<=1000 and 1<=nextj<=1000 and not graph[nexti][nextj]:
                graph[nexti][nextj]=graph[s1][s2]+1
                queue.append((nexti,nextj))

# A* 算法
import heapq
 
n = int(input())
 
moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
 
def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
 
def bfs(start, end):
    q = [(distance(start, end), start)]
    step = {start: 0}
     
    while q:
        d, cur = heapq.heappop(q)
        if cur == end:
            return step[cur]
        for move in moves:
            new = (move[0] + cur[0], move[1] + cur[1])
            if 1 <= new[0] <= 1000 and 1 <= new[1] <= 1000:
                step_new = step[cur] + 1
                if step_new < step.get(new, float('inf')):
                    step[new] = step_new
                    heapq.heappush(q, (distance(new, end) + step_new, new))
    return False
                     
for _ in range(n):
    a1, a2, b1, b2 = map(int, input().split())
    print(bfs((a1, a2), (b1, b2)))
