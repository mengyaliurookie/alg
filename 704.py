
# 递归版本
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binsearch(nums,0,len(nums)-1,target)
    def binsearch(self,nums,left,right,target):
        if left>right: return -1
        mid=int((left+right)/2)
        # print('left:',left)
        # print('right:',right)
        # print('mid:',mid)
        if target<nums[mid]:
            right=mid-1
        elif target>nums[mid]:
            left=mid+1
        else:
            return mid
        return self.binsearch(nums,left,right,target)


# 迭代版本，需要注意的是，fir和sec的关系，fir要小于等于sec，这样才能把fir和sec相等的地方也进行判断
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        fir=0
        sec=len(nums)-1
        res=-1
        while fir<=sec:
            mid=int((fir+sec)/2)
            if nums[mid]>target:
                sec=mid-1
            elif nums[mid]<target:
                fir=mid+1
            else:
                res=mid
                break
        return res