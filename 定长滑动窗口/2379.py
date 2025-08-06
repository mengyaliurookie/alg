class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 翻译一下题意，就是需要找到连续k个字符中，黑色块最多的
        right=0
        ans=0
        res=k+1
        n=len(blocks)
        while right<n:
            if right-k+1<0:
                if blocks[right]=='W': ans+=1
                right+=1
                continue
            # 此时窗口已经到达k
            if blocks[right]=='W':
                ans+=1
            res=min(res,ans)
            if blocks[right-k+1]=='W': ans-=1
            right+=1
        return res