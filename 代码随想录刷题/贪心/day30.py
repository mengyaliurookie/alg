
# 452. 用最少数量的箭引爆气球
topic="""
有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。

一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。

给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。

 
示例 1：

输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用2支箭来爆破:
-在x = 6处射出箭，击破气球[2,8]和[1,6]。
-在x = 11处发射箭，击破气球[10,16]和[7,12]。
示例 2：

输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要4支箭。
示例 3：

输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处射出箭，击破气球[3,4]和[4,5]。
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 一支箭可以射穿的终止条件是什么，打到之后就可以加一
        # 先排序，遇到一个终点的话，必须要判断了，要不要发射一个新的箭头
        # 那就需要依靠之前的处理
        # 从头开始遇到第一个终点，那必须要发射，发射之后，要记录上一个发射的终点值，如果下一个终点的范围包括上一个，那就不需要发射
        points.sort(key=lambda x:x[1])
        # print(points)
        lastp=float('-inf')
        ans=0
        for p in points:
            if lastp==float('-inf'):
                # 第一个点必须发射
                lastp=p[1]
                ans+=1
            else:
                # 否则需要判断要不要发射
                if p[0]<=lastp and p[1]>=lastp:
                    # 如果上一次发射的位置在这个气球的范围内，就不需要发射
                    continue
                else:
                    ans+=1
                    lastp=p[1]
        return ans

# 435. 无重叠区间
topic="""
给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。

注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。

 

示例 1:

输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: intervals = [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 还是要排序，才能找到重叠的情况，遇到重叠的就需要移除区间，或者保留，只保留
        intervals.sort(key=lambda x:(x[1],x[0]))
        # 遇到重叠的，那只能保留一个的话，那保留右边界最小的肯定是对后序影响最小的
        print(intervals)
        lastp=intervals[0][1]
        n=len(intervals)
        ans=0
        for i in range(1,n):
            if intervals[i][1]==lastp:
                ans+=1
                continue
            if lastp>intervals[i][0] and lastp<intervals[i][1]:
                # 此时重叠了
                # 需要去除这个更大的元素
                ans+=1
            else:
                # 否则更新lastp
                lastp=intervals[i][1]
        return ans


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 按右端点升序
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        ans = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # 重叠，删除当前区间
                ans += 1
            else:
                # 不重叠，保留，更新 end
                end = intervals[i][1]

        return ans


# 763.划分字母区间
topic="""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

返回一个表示每个字符串片段的长度的列表。

 

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 
示例 2：

输入：s = "eccbbbbdec"
输出：[10]
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 相当于求并集
        dic=dict()
        for i,v in enumerate(s):
            if v in dic:
                dic[v].append(i)
            else:
                dic[v]=[i]
        # print(dic)
        l=[]
        for k,v in dic.items():
            if len(v)==1:
                l.append([v[0],v[0]])
            else:
                l.append([v[0],v[-1]])
        # print(l)
        # 然后求并集
        l.sort()
        ln=len(l)
        fir=l[0][0]
        sec=l[0][1]
        ans=[]
        for f in range(1,ln):
            if l[f][0]<=sec:
                sec=max(l[f][1],sec)
            else:
                ans.append([fir,sec])
                fir=l[f][0]
                sec=l[f][1]
        # print(ans)
        res=[]
        for a in ans:
            res.append(a[1]-a[0]+1)
        if ans:
            res.append(len(s)-ans[-1][1]-1)
        else:
            res.append(len(s))
        return res

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 相当于求并集
        dic=dict()
        for i,v in enumerate(s):
            dic[v]=i
        right=0
        ans=[-1]
        for i,v in enumerate(s):
            right=max(dic[v],right)
            if i==right:
                ans.append(right)
        res=[]
        # print(ans)
        n=len(ans)
        for i in range(1,n):
            res.append(ans[i]-ans[i-1])
        return res


