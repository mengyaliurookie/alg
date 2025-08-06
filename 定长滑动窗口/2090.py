class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # 可以转化为普通的定长滑动窗口问题
        dk = 2 * k + 1
        res = [-1] * len(nums)
        ans = []
        sum = 0
        for i, v in enumerate(nums):
            if i - dk + 1 < 0:
                sum += v
                continue
            sum += v
            ans.append(int(sum / dk))
            sum -= nums[i - dk + 1]
        for i, v in enumerate(ans):
            res[i + k] = v
        return res
