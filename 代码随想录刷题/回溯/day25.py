
# 37. 解数独
topic="""
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

 

示例 1：


输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 使用集合记录每行、每列、每宫格已使用的数字
        row_used = [set() for _ in range(9)]  # row_used[i] 表示第 i 行已用的数字（字符串）
        col_used = [set() for _ in range(9)]  # 第 j 列
        box_used = [set() for _ in range(9)]  # 第 k 个 3x3 宫格

        # 初始化已用数字
        empty_cells = []  # 存储空格位置 (i, j)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    row_used[i].add(num)
                    col_used[j].add(num)
                    box_idx = (i // 3) * 3 + (j // 3)
                    box_used[box_idx].add(num)
                else:
                    empty_cells.append((i, j))

        def get_candidates(i, j):
            """获取位置 (i,j) 的候选数字"""
            box_idx = (i // 3) * 3 + (j // 3)
            used = row_used[i] | col_used[j] | box_used[box_idx]
            return [str(num) for num in range(1, 10) if str(num) not in used]

        def dfs():
            if not empty_cells:
                return True  # 所有空格已填

            # 找出候选数最少的空格（MRV启发式）
            min_candidate_cell = None
            min_candidates = None
            candidates_list = []
            for cell in empty_cells:
                i, j = cell
                cands = get_candidates(i, j)
                if len(cands) == 0:
                    return False  # 无解
                if min_candidate_cell is None or len(cands) < len(min_candidates):
                    min_candidate_cell = cell
                    min_candidates = cands
                    candidates_list = cands

            i, j = min_candidate_cell
            box_idx = (i // 3) * 3 + (j // 3)

            # 尝试每一个候选数
            for num in candidates_list:
                # 剪枝：尝试放 num
                board[i][j] = num
                row_used[i].add(num)
                col_used[j].add(num)
                box_used[box_idx].add(num)
                empty_cells.remove((i, j))

                if dfs():
                    return True

                # 回溯
                board[i][j] = '.'
                row_used[i].remove(num)
                col_used[j].remove(num)
                box_used[box_idx].remove(num)
                empty_cells.append((i, j))

            return False

        dfs()
