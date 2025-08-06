
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


# 27 移除元素
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 使用双指针，找到开头第一个等于target的元素位置，同时找到结尾第一个不等于target的元素
        # 然后交换元素，直到遍历完所有元素
        target=val
        fir=0
        sec=len(nums)-1
        while fir<=sec:
            while fir<=sec and nums[fir]!=target:
                fir+=1
            # 此时fir指向的元素一定等于target
            while fir<=sec and nums[sec]==target:
                sec-=1
            if fir<=sec:
                # 交换位置
                nums[fir],nums[sec]=nums[sec],nums[fir]
                # 此时fir位置处一定不为target
                fir+=1
                # 此时sec位置一定为target
                sec-=1
        k=len(nums)
        for i,v in enumerate(nums):
            if v==target:
                k=i
                break
        return k

# 977 有序数组的平方
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 因为有负数，所以需要找到正负数交汇的地方，然后向两边遍历
        # 很像归并排序中的合并阶段
        # 先找到第一个正数
        fir = len(nums)
        for i, v in enumerate(nums):
            if v > 0:
                fir = i
                break
        # 然后找到负数的位置
        sec = fir - 1
        ans = []
        while sec > -1 and fir < len(nums):
            if nums[sec] * nums[sec] > nums[fir] * nums[fir]:
                ans.append(nums[fir] * nums[fir])
                fir += 1
            else:
                ans.append(nums[sec] * nums[sec])
                sec -= 1
        while sec > -1:
            ans.append(nums[sec] * nums[sec])
            sec -= 1
        while fir < len(nums):
            ans.append(nums[fir] * nums[fir])
            fir += 1
        return ans




