class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        ans = []
        n = len(graph)

        def dfs(i):
            # 将当前节点加入到路径中
            path.append(i)
            # 如果到达最终节点，那么需要把路径添加到结果中
            if i == n - 1:
                ans.append(path.copy())
            # 因为没有环，所以必然会到达一个没有出度的节点，所以不需要记录是否访问过某个节点，会终止返回
            for j in graph[i]:
                dfs(j)
            path.pop()

        dfs(0)
        return ans
