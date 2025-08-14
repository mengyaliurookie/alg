
# 151.翻转字符串里的单词
topic="""
    给你一个字符串 s ，请你反转字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

 

示例 1：

输入：s = "the sky is blue"
输出："blue is sky the"
示例 2：

输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # 好像可以先整体反转一遍，然后再单独每个单词反转一边，最后再把空格去除
        sl = list(s)
        n = len(sl)
        # 先把空格调整了

        # print(sl)
        slr = sl[::-1]
        # 然后反转里面的每个单词
        fir = 0
        sec = 0

        while sec < n:
            # 用双指针来确认单词的起始位置
            # 如果第一个位置上是空格，那么就一起移动，直到第一个指向非空格，再移动sec到空格，这样才能确认一个的单词
            if fir < n and slr[fir] == ' ':
                fir += 1
                sec += 1
            # 到达此处的时候fir是不为空格的，此时移动sec到下一个空格或者到达末尾
            while sec < n and slr[sec] != ' ':
                sec += 1
            # 此时要么sec为n或者sec指向空格
            # 只需要交换sec-1和fir指向的元素就可以
            tem1 = fir
            tem2 = sec - 1
            while tem1 < tem2:
                slr[tem1], slr[tem2] = slr[tem2], slr[tem1]
                tem1 += 1
                tem2 -= 1
            # 交换完毕之后，把fir更新到sec
            fir = sec
        # print(slr)
        # 然后就是移除空格，也是采用双指针的方式，找到第一个可以替换的位置，和下一个不是空格的位置
        # 第一个可以替换的位置，包括开头的空格，和中间的第二个空格
        # 感觉比较麻烦，可以通过插入空格的方式来处理
        # 碰到空格就
        write = 0
        for read in range(n):
            if slr[read] != ' ':  # 非空格，直接写入
                slr[write] = slr[read]
                write += 1
            else:  # 当前是空格
                if write > 0 and slr[write - 1] != ' ':  # 前一个不是空格，才写入一个空格
                    slr[write] = ' '
                    write += 1
        res = slr[:write]
        jq = 0
        for j in range(len(res) - 1, -1, -1):
            if res[j] == ' ':
                jq += 1
            else:
                break
        res = res[:len(res) - jq]
        return "".join(res)


# 右旋字符串
topic="""
    字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。

例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。

输入：输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。

输出：输出共一行，为进行了右旋转操作后的字符串。

样例输入：

2
abcdefg 
样例输出：

fgabcde
"""
def main():
    k=int(input().strip())
    s=input().strip()
    n=len(s)
    sl=list(s)
    fir=0
    sec=n-1
    while fir<sec:
        sl[fir],sl[sec]=sl[sec],sl[fir]
        fir+=1
        sec-=1
    fir=0
    sec=k-1
    while fir<sec:
        sl[fir],sl[sec]=sl[sec],sl[fir]
        fir+=1
        sec-=1
    fir=k
    sec=n-1
    while fir<sec:
        sl[fir],sl[sec]=sl[sec],sl[fir]
        fir+=1
        sec-=1
    print("".join(sl))

if __name__=="__main__":
    main()


# 459.重复的子字符串
















