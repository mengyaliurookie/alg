class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        it = int(n / 2)
        # 起始点x,y
        # 然后是拐点
        res = [[0 for _ in range(n)] for _ in range(n)]
        x = 0
        y = 0
        u = 1
        leftx = 0
        lefty = 0
        rightx = n - 1
        righty = n - 1
        while it:
            while y < righty:
                # print("x: ",x)
                # print("y: ",y)
                # print('u',u)
                # print()
                res[x][y] = u
                u += 1
                y += 1
            while x < rightx:
                # print("x: ",x)
                # print("y: ",y)
                # print('u',u)
                # print()
                res[x][y] = u
                u += 1
                x += 1
            while y > lefty:
                # print("x: ",x)
                # print("y: ",y)
                # print('u',u)
                # print()
                res[x][y] = u
                u += 1
                y -= 1
            while x > leftx:
                # print("x: ",x)
                # print("y: ",y)
                # print('u',u)
                # print()
                res[x][y] = u
                u += 1
                x -= 1
            it -= 1
            x += 1
            y += 1
            leftx += 1
            lefty += 1
            rightx -= 1
            righty -= 1
        if n % 2 == 1:
            res[int(n / 2)][int(n / 2)] = n * n
        return res





