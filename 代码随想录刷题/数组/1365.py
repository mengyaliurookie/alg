class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 首先排序之后
        tem=sorted(nums)
        dic=dict()
        for i,v in enumerate(tem):
            if v in dic.keys():
                continue
            dic[v]=i
        res=[]
        for i in nums:
            res.append(dic[i])
        return res
