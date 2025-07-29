class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        # 先遍历，目的是找到每个元素右边第一个比它大的元素，找到之后，就可以把比这个元素小的元素弹出了
        # 因为可以直接计算它们之间可以接多少雨水了
        res = 0
        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                # 坑底
                bottom = stack.pop()
                # 没有左墙退出循环
                if not stack:
                    break
                # 有左墙计算蓄水量
                left = height[stack[-1]]
                right = h
                w = i - stack[-1] - 1
                hei = min(h, height[stack[-1]]) - height[bottom]
                res += w * hei
            stack.append(i)

        return res