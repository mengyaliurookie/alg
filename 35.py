class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first=0
        sec=len(nums)-1
        res=-1
        while first<=sec:
            mid=int((first+sec)/2)
            # print("fir: ",first)
            # print("sec: ",sec)
            # print("mid: ",mid)
            tem=nums[mid]
            if tem==target:
                res=mid
                break
            elif tem<target:
                first=mid+1
            else:
                sec=mid-1
        # print("fir: ",first)
        # print("sec: ",sec)
        # print("mid: ",mid)
        return res if res!=-1 else first