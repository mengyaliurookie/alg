class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 只要局部和小于零，那么就不会是最大连续子数组的一部分
        psum = nums[0]
        first = 0
        sec = 0
        res = max(psum, float('-inf'))
        n = len(nums)
        while sec < n:
            if psum < 0:
                sec += 1
                first = sec
                if sec < n:
                    psum = nums[sec]
                res = max(res, psum)
            else:
                sec += 1
                if sec < n:
                    psum += nums[sec]
                res = max(res, psum)
        return res
