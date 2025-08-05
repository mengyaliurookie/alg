class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target=threshold*k
        ans=0
        sum=0
        for i,v in enumerate(arr):
            if i-k+1<0:
                sum+=v
                continue
            sum+=v
            if target<=sum:
                ans+=1
            sum-=arr[i-k+1]
        return ans