
# 332.重新安排行程
topic="""
    给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。

所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。

例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。

 

示例 1：


输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
输出：["JFK","MUC","LHR","SFO","SJC"]
示例 2：


输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
"""
# 这种写法会超时，
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 一种暴力的方式是把所有情况进行全排列，然后找出一条是从JFK出发的，并且可以走通的路
        n=len(tickets)
        ans=[]
        path=[]
        def isvalid(tickets):
            # 前一张票的终点，是后一张票的起点，否则不是有效的形成组合
            ans=True
            for i,v in enumerate(tickets):
                if i>0:
                    if v[0]!=tickets[i-1][1]:
                        ans=False
                        break
            return ans
        def getans(tickets):
            ans=[]
            n=len(tickets)
            for i,v in enumerate(tickets):
                if i<n-1:
                    ans.append(v[0])
                else:
                    ans.extend(v)
            return ans
        used=[False]*n
        def dfs(d,last):
            if d==n:
                if path[0][0]=='JFK' and isvalid(path):
                    ans.append(getans(path))
                return
            # if d==1 and last[0]!='JFK':
            #     return
            for i in range(n):
                if d==0 and tickets[i][0]!='JFK':
                    continue
                # 剪枝，当前一张票和后一张票不能成功连通就直接跳过
                if last and last[1]!=tickets[i][0]:
                    continue
                if not used[i]:
                    used[i]=True
                    path.append(tickets[i])
                    dfs(d+1,tickets[i])
                    path.pop()
                    used[i]=False
        dfs(0,None)
        # print(ans)
        ans.sort()
        return ans[0]

# 改进了，但是还是会超时
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 一种暴力的方式是把所有情况进行全排列，然后找出一条是从JFK出发的，并且可以走通的路
        n = len(tickets)
        ans = []
        path = ['JFK']
        # 直接全排列的方式会超时
        # 看了部分题解的大概用了什么数据结构，所以尝试改进一下
        # 用一个字典，key是各个点，然后v是从key出发可以到达的点
        dic = defaultdict(list)
        for t in tickets:
            dic[t[0]].append(t[1])
        # 然后对字典中的列表进行排序
        used = {}
        for k, v in dic.items():
            dic[k].sort()
            used[k] = [False] * len(v)
        print(dic)

        # 然后从JFK开始进行dfs
        # 还要避免重复使用同一张票
        def dfs(i, key):
            if i == n and not ans:
                ans.append(path[:])
                return
            if ans: return
            layer = dic[key]
            m = len(layer)
            for j in range(m):
                if not used[key][j]:
                    used[key][j] = True
                    path.append(layer[j])
                    dfs(i + 1, layer[j])
                    path.pop()
                    used[key][j] = False

        dfs(0, 'JFK')
        return ans[0]

# 这样才不会超时，核心关键是有明确的入队时机，这样就可以遍历一次就可以了。
# 而回溯的方式，只有在最后的时候才会判断，或者中间加一些剪枝，但是如果先走到死胡同，那还是会回溯到正确的位置，然后走，最终还是会走一遍之前走的死胡同。所以会重复走。
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 一种暴力的方式是把所有情况进行全排列，然后找出一条是从JFK出发的，并且可以走通的路
        # 直接全排列的方式会超时
        # 看了部分题解的大概用了什么数据结构，所以尝试改进一下
        # 用一个字典，key是各个点，然后v是从key出发可以到达的点
        dic=defaultdict(list)
        for t in tickets:
            dic[t[0]].append(t[1])
        # 然后对字典中的列表进行排序
        for k,v in dic.items():
            dic[k].sort(reverse=True)
        # 然后从JFK开始进行dfs
        # 还要避免重复使用同一张票
        queue=deque()
        def dfs(key):
            while dic[key]:
                nextnode=dic[key].pop()
                dfs(nextnode)
            queue.appendleft(key)
        dfs('JFK')
        return list(queue)