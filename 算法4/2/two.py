from typing import List

class Example:

    def __init__(self):
        pass

    def sort(self,nums:List)->None:
        pass

    def less(self,a,b):
        return a<=b

    def exch(self,nums:List,i:int,j:int):
        nums[i],nums[j]=nums[j],nums[i]

    def show(self,nums:List):
        for v in nums:
            print(v,end=" ")
        print()

    def isSorted(self,nums:List):
        n=len(nums)
        for i in range(1,n):
            if (self.less(nums[i-1],nums[i])): return True
        return True

# 2.1.2 选择排序
# 一种最简单的排序算法是这样的，首先，找到数组中最小的那个元素，其次，将它和数组的第一个元素交换位置。
# 再次，在剩下的元素中找到最小的元素，将它与数组中的第二个元素交换位置。
# 如此往复，直到将整个数组排序。

class Selection:

    def __init__(self,nums):
        self.nums=nums

    def sort(self):
        n=len(self.nums)
        for i in range(n):
            min=i
            for j in range(i+1,n):
                if self.nums[min]>self.nums[j]: min=j
            self.exch(self.nums,i,min)
    def exch(self,nums:List,i:int,j:int):
        nums[i],nums[j]=nums[j],nums[i]

    def show(self):
        for v in self.nums:
            print(v,end=" ")
        print()

s=Selection([7,6,8,3,9])
s.sort()
s.show()


class Shell:

    def __init__(self,nums):
        self.nums=nums

    def sort(self):
        n=len(self.nums)
        h=1
        while h<int(n/3):
            h=3*h+1
        while(h>=1):
            for i in range(h,n):
                j=i
                while j>=h and self.nums[j]<self.nums[j-h]:
                    self.exch(j,j-h)
                    j-=h
            h=int(h/3)
    def exch(self, i: int, j: int):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def show(self):
        for v in self.nums:
            print(v,end=" ")
        print()


s=Shell([7,6,8,3,9])
s.sort()
s.show()
