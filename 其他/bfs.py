from collections import deque

# x轴向下，y轴向右
# 四个方向数组：右、左、下、上（对应原C++代码的四个方向）
directions=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(grid:list[list[str]],visited:list[list[bool]],x:int,y:int)->None:
    """
    BFS遍历二维网络
    参数说明：
        grid:二维字符数组，表示地图
        visited:二维布尔数组，记录节点访问状态
        x，y：起始坐标
    """
    # 初始化队列（使用Python的deque优化队列操作）
    que=deque()
    que.append((x,y))    #将起始点加入队列
    visited[x][y]=True   #立刻标记已访问

    # 获取网络尺寸（提前计算避免重复调用）
    rows=len(grid)
    cols=len(grid[0] if rows>0 else 0)
    while que:
        cur=que.popleft() #取出队列首部元素
        cur_x,cur_y=cur #解包当前坐标

        # 遍历四个方向
        for dx,dy in directions:
            nx,ny=cur_x+dx,cur_y+dy
            # 判断是否越界
            if nx<0 or nx>=rows or ny<0 or ny>=cols:
                continue
            # 判断是否已访问
            if not visited[nx][ny]:
                que.append((nx,ny)) #加入队列
                visited[nx][ny]=True #立刻标记已访问
