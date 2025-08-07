from typing import List

# 209 长度最小的子数组
job="""给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 变长滑动窗口
        # 变长相对于定长来说，就是入和出都是可以很多个，不是每次只入一个出一个
        n = len(nums)
        ans = n + 1  # 结果
        res = 0  # 记录中间窗口内的元素的和
        right = 0  # 右端点的索引值
        left = 0  # 左端点的索引值，因为是变长的，所以不能根据右端点直接计算出来，所以需要单独记录一下
        while right < n:
            while right < n and res < target:
                # 如果当前窗口结果小于目标值，那么就把右端点加入到窗口中，同时把右端点的索引右移
                res += nums[right]
                right += 1
            # 如果到达这里，说明此时窗口内的值得和是大于等于target的
            # 此时，需要更新ans的值
            # ans=min(ans,right-left)
            # 然后需要移出左侧的值。看是不是有更短的满足的情况
            # 这里是一次只移出一个吗，不，应该一直移出，因为如果根据大循环的话，那么当right到达末尾之后，可能就不会再移动左端点了
            while left < right and res >= target:
                ans = min(ans, right - left)
                res -= nums[left]
                left += 1

        return 0 if ans == n + 1 else ans


# 59 螺旋矩阵II
job="""给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 找循环不变量
        # 圈数r=int(n/2)
        r = int(n / 2)
        # 找有规律的变量，比如每一圈开始的行号，列号，每个方向遍历的数量
        inc = n - 1
        # 定义一个结果二维数组
        res = [[0] * n for _ in range(n)]
        st = 1
        for i in range(r):
            row = i
            col = i
            # 从左向右，行不变，列向右，以及向右的长度
            for j in range(0, inc):
                res[row][col + j] = st
                st += 1
            # 在此更新col
            col = col + j + 1
            # 从上到下，行向下，列在上面从左到右的基础上不变
            for k in range(inc):
                res[row + k][col] = st
                st += 1
            # 在此更新row
            row = row + k + 1
            # 从右向左，行不变，列从右向左减小
            for l in range(inc):
                res[row][col - l] = st
                st += 1
            # 在此更新col
            col = col - l - 1
            # 从下向上，列不变，行从下往上
            for m in range(inc):
                res[row - m][col] = st
                st += 1
            # 一圈遍历完了，需要更新inc
            inc -= 2
        # 最如果是奇数的话，需要补全一下中间的
        if n % 2 == 1:
            res[int(n / 2)][int(n / 2)] = st
        return res


# 58. 区间和
job="""题目描述
给定一个整数数组 Array，请计算该数组在每个指定区间内元素的总和。
输入描述
第一行输入为整数数组 Array 的长度 n，接下来 n 行，每行一个整数，表示数组的元素。随后的输入为需要计算总和的区间下标：a，b （b > = a），直至文件结束。
输出描述
输出每个指定区间内元素的总和。
输入示例
5
1
2
3
4
5
0 1
1 3
输出示例
3
9"""


def main():
    # 输入数据的长度
    n = int(input())
    # print(n)
    # 初始化前缀和数组
    rl = []
    for i in range(n):
        rl.append(int(input()))
    res = [0] * len(rl)
    for i in range(n):
        if i != 0:
            res[i] = res[i - 1] + rl[i]
        else:
            res[i] = rl[i]
    # print(res)
    while True:
        try:
            nums = input().strip().split()
        except:
            break
        if int(nums[0]) == 0:
            print(res[int(nums[1])])
        else:
            print(res[int(nums[1])] - res[int(nums[0]) - 1])


# 44. 开发商购买土地

job="""题目描述
在一个城市区域内，被划分成了n * m个连续的区块，每个区块都拥有不同的权值，代表着其土地价值。目前，有两家开发公司，A 公司和 B 公司，希望购买这个城市区域的土地。 

现在，需要将这个城市区域的所有区块分配给 A 公司和 B 公司。

然而，由于城市规划的限制，只允许将区域按横向或纵向划分成两个子区域，而且每个子区域都必须包含一个或多个区块。 为了确保公平竞争，你需要找到一种分配方式，使得 A 公司和 B 公司各自的子区域内的土地总价值之差最小。 

注意：区块不可再分。

输入描述
第一行输入两个正整数，代表 n 和 m。 

接下来的 n 行，每行输出 m 个正整数。

输出描述
请输出一个整数，代表两个子区域内土地总价值之间的最小差距。
输入示例
3 3
1 2 3
2 1 3
1 2 3
输出示例
0"""

import copy


def main():
    # 读入行数和列数
    n, m = [int(i.strip()) for i in input().split()]
    # 根据行数读入数据
    d = []
    for i in range(n):
        tem = [int(i.strip()) for i in input().split()]
        d.append(tem)
    # 模拟一下这个过程
    # 选一个分界线，然后利用前缀和可以方便的求出两个区域的面积，然后就可以方便的求出面积的差
    # 然后再求出横着的
    # 先竖着划线，范围0，1，2左闭右开，表示其中一个区域，剩下的是另一个区域
    # 先求前缀和
    rowsum = copy.deepcopy(d)
    for i in range(1, m):
        for j in range(n):
            rowsum[j][i] += rowsum[j][i - 1]
    # 开始划分区域，竖着
    res = float('inf')
    for i in range(1, m):
        area1 = 0
        area2 = 0
        for j in range(n):
            area1 += rowsum[j][i - 1]
            area2 += rowsum[j][m - 1] - rowsum[j][i - 1]
        # 此时已经计算出来两个区域的面积
        res = min(res, abs(area1 - area2))
    # 开始计算横着划线的方式
    colsum = copy.deepcopy(d)
    for i in range(1, n):
        for j in range(m):
            colsum[i][j] += colsum[i - 1][j]
    for i in range(1, n):
        area1 = 0
        area2 = 0
        for j in range(m):
            area1 += colsum[i - 1][j]
            area2 += colsum[n - 1][j] - colsum[i - 1][j]
        # 此时已经计算出来两个区域的面积
        res = min(res, abs(area1 - area2))
    return res


if __name__ == '__main__':
    print(main())
