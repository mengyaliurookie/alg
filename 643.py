class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 平均数可以转换为sum最大，因为都是在求sum/k
        ans = -100000 * k
        sum = 0
        for i, v in enumerate(nums):
            if i - k + 1 < 0:
                sum += v
                continue
            # 移入当前元素
            sum += v
            ans = max(sum, ans)
            # 移出窗口左端元素
            sum -= nums[i - k + 1]
        return ans / k

