class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 可以先实现一个字典里面存的是各个元素的个数，时间复杂度是O(n)的，
        # 然后找出前k个元素的话，需要用一个单调栈来实现？
        count = Counter()
        for i in nums:
            count[i] += 1

        # 翻转字典的key和value
        ind = defaultdict(list)
        for key, value in count.items():
            ind[value].append(key)
        sk = list(ind.keys())
        sk.sort(reverse=True)
        res = []
        cnt = 0
        while len(res) < k and cnt != k:
            res.extend(ind[sk[cnt]])
            cnt += 1

        # 先确定比较规则，如果当前元素大于里面的元素，那么里面的元素要出去，可以用两个栈来实现

        return res
