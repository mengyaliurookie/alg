

# 344.反转字符串
topic="""
    编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

 

示例 1：

输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 使用双指针的方式交换收尾元素
        fir=0
        sec=len(s)-1
        while fir<sec:
            s[fir],s[sec]=s[sec],s[fir]
            fir+=1
            sec-=1


# 541. 反转字符串II
topic="""
    给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 

示例 1：

输入：s = "abcdefg", k = 2
输出："bacdfeg"
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        sl = [i for i in s]

        for start in range(0, n, k):
            # print('start: ',start)
            if (start / k) % 2 == 0:
                fir = start
                sec = min(start + k - 1, n - 1)
                while fir < sec:
                    sl[fir], sl[sec] = sl[sec], sl[fir]
                    fir += 1
                    sec -= 1
        return "".join(sl)

topic="""
54. 替换数字（第八期模拟笔试）
题目描述
给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。 例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。
输入描述
输入一个字符串 s,s 仅包含小写字母和数字字符。
输出描述
打印一个新的字符串，其中每个数字字符都被替换为了number
输入示例
a1b2c3
输出示例
anumberbnumbercnumber
"""

def main():
    s=input().strip()
    sl=[]
    for i in s:
        if i.isdigit():
            sl.append("number")
        else:
            sl.append(i)
    print("".join(sl))

if __name__=="__main__":
    main()