# 42. 接雨水
topic="""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        # 先遍历，目的是找到每个元素右边第一个比它大的元素，找到之后，就可以把比这个元素小的元素弹出了
        # 因为可以直接计算它们之间可以接多少雨水了
        res=0
        for i,h in enumerate(height):
            while stack and h>=height[stack[-1]]:
                # 坑底
                bottom=stack.pop()
                # 没有左墙退出循环
                if not stack:
                    break
                # 有左墙计算蓄水量
                left=height[stack[-1]]
                right=h
                w=i-stack[-1]-1
                hei=min(h,height[stack[-1]])-height[bottom]
                res+=w*hei
            stack.append(i)
                
        return res

# 84.柱状图中最大的矩形
topic="""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

示例 1:



输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：



输入： heights = [2,4]
输出： 4
"""
 # 之前想到的思路是对的，但是只是在等于那里不知道怎么处理了
# 其实只要保证栈中的顺序也是严格的就可以
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 一个元素的长需要在左侧查找第一个小于的和右侧第一个小于的，高就是自己
        # 所以需要找到从左往右第一个比自己小的
        # 然后再找到从右往左第一个比自己小的
        n=len(heights)
        ansl=[n]*n
        ansr=[-1]*n
        ans=[]
        stack=[]
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                # 此时需要记录栈顶元素的右侧第一个比自己小的元素的索引
                ind=stack.pop()
                ansl[ind]=i
            # 否则就入栈
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            # print(f'stack: {stack}')
            while stack and heights[i]<heights[stack[-1]]:
                # 此时需要记录栈顶元素的右侧第一个比自己小的元素的索引
                ind=stack.pop()
                ansr[ind]=i
            # 否则就入栈
            stack.append(i)
        # print(ansl)
        # print(ansr)
        for i in range(n):
            ans.append(heights[i]*(ansl[i]-ansr[i]-1))
        
        return max(ans)
