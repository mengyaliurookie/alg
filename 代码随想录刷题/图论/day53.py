# 110. 字符串接龙
topic="""
题目描述
字典 strList 中从字符串 beginStr 和 endStr 的转换序列是一个按下述规格形成的序列： 



1. 序列中第一个字符串是 beginStr。

2. 序列中最后一个字符串是 endStr。 

3. 每次转换只能改变一个字符。 

4. 转换过程中的中间字符串必须是字典 strList 中的字符串，且strList里的每个字符串只用使用一次。 



给你两个字符串 beginStr 和 endStr 和一个字典 strList，找到从 beginStr 到 endStr 的最短转换序列中的字符串数目。如果不存在这样的转换序列，返回 0。

输入描述
第一行包含一个整数 N，表示字典 strList 中的字符串数量。 第二行包含两个字符串，用空格隔开，分别代表 beginStr 和 endStr。 后续 N 行，每行一个字符串，代表 strList 中的字符串。
输出描述
输出一个整数，代表从 beginStr 转换到 endStr 需要的最短转换序列中的字符串数量。如果不存在这样的转换序列，则输出 0。
输入示例
6
abc def
efc
dbc
ebc
dec
dfc
yhn
输出示例
4
提示信息
从 startStr 到 endStr，在 strList 中最短的路径为 abc -> dbc -> dec -> def，所以输出结果为 4，如图：

数据范围：

2 <= N <= 500
"""

import sys
from collections import Counter,deque
import math

def isok(a, b):
    """判断两个字符串是否只相差一个字符"""
    if len(a) != len(b):
        return False
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            if diff > 1:
                return False
    return diff == 1


def main():
    n=int(input())
    beginStr,endStr=input().strip().split()
    bag={}
    for _ in range(n):
        tstr=input().strip()
        bag[tstr]=0
    # =0表示还可以选
    # print(f"bag = {bag}")
    ans=math.inf
    def bfs():
        queue=deque()
        queue.append((beginStr,1))
        while queue:
            word,step=queue.popleft()
            if isok(word,endStr):
                return step+1
            for s,i in bag.items():
                if i==0 and isok(s,word):
                    queue.append((s,step+1))
                    bag[s]=1
        return -1
    ans=bfs()
    if ans==-1:
        print(0)
    else:
        print(ans)







