# 正常for循环遍历
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                continue
        continue
    return False


# 二分查找
# def binarySearch(matrix, target):
#     """
#     :type matrix: List[List[int]]
#     :type target: int
#     :rtype: bool
#     """
#     m = len(matrix)
#     if m == 0:
#         return False
#     n = len(matrix[0])
#
#     # 设置指针
#     row = m - 1
#     col = 0
#     while col < n and row >= 0:
#         print(row, col)
#         if matrix[row][col] > target:
#             row -= 1
#             print(row, col)
#         elif matrix[row][col] < target:
#             col += 1
#             print(row, col)
#         else:
#             return True
#     return False


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    matrix1 = [[], []]
    target = 15
    res = searchMatrix(matrix1, target)
    print(res)
    # res = binarySearch(matrix, target)
    print(res)
