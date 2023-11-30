# 1727 Largest Submatrix With Rearrangements
# Difficulty: Medium

"""
You are given a binary matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
Return the area of the largest sub-matrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
"""

def consecutive_ones_row(matrix, i, j):
    """
    This function returns the number of consecutive ones in a row starting from the [i][j] element.
    It takes as input a matrix and the starting indices i and j.
    If the matrix is empty or the first row is empty, it returns 0.
    Otherwise, it counts the number of consecutive ones in the row starting from the [i][j] element and returns this count.
    """
    if not matrix or not matrix[0]:
        return 0

    count = 0
    while j < len(matrix[0]) and matrix[i][j] == 1:
        count += 1
        j += 1

    return count


def consecutive_ones_col(matrix, i, j):
    """
    This function returns the number of consecutive ones in a column starting from the [i][j] element.
    It takes as input a matrix and the starting indices i and j.
    If the matrix is empty or the first row is empty, it returns 0.
    Otherwise, it counts the number of consecutive ones in the column starting from the [i][j] element and returns this count.
    """
    if not matrix or not matrix[0]:
        return 0

    count = 0
    while i < len(matrix) and matrix[i][j] == 1:
        count += 1
        i += 1

    return count


def eval_matrix(matrix):
    """
    This function evaluates the area of the largest sub-matrix with all ones in the given matrix.
    It takes as input a binary matrix.
    If the matrix is empty or the first row is empty, it returns 0.
    Otherwise, it scans the matrix by row from left to right.
    If the current element is 1, it checks at its right and down.
    The sub-matrix can be expanded to these two directions.
    The function will return the area of the biggest sub-matrix found.
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    i = 0  # row index
    j = 0  # column index
    max_area = 0

    while i < m:
        if matrix[i][j] == 0:
            if j + 1 < n:
                j += 1
            else:
                i += 1
                j = 0

            continue
        else:
            max_row_dimension = consecutive_ones_row(matrix, i, j)
            max_col_dimension = consecutive_ones_col(matrix, i, j)

            max_area = max(max_row_dimension, max_col_dimension, max_area)
            i_sub = 1  # column index for sub-matrix expansion
            while i_sub < max_col_dimension:
                sub_row_dimension = min(consecutive_ones_row(matrix, i + i_sub, j), max_row_dimension)
                if sub_row_dimension * (i_sub + 1) > max_area:
                    max_area = sub_row_dimension * (i_sub + 1)
                    max_row_dimension = sub_row_dimension
                i_sub += 1

            if j + 1 < n:
                j += 1
            else:
                i += 1
                j = 0

    return max_area


def matrix_column_permutation(matrix, permutation):
    """
    This function returns the matrix with the columns permuted according to the permutation list.
    It takes as input a matrix and a permutation list.
    It generates a new matrix with the columns permuted according to the permutation and returns this new matrix.
    """
    m, n = len(matrix), len(matrix[0])
    new_matrix = []
    for i in range(m):
        new_matrix.append([matrix[i][permutation[j]] for j in range(n)])

    return new_matrix


def all_permutations(n):
    """
    This function returns all possible permutations of the list [0:n].
    It takes as input an integer n.
    It generates all possible permutations of the list [0:n] and returns these permutations.
    """
    def permute(data, i, length):
        if i==length:
            permutations.append(data.copy())
        else:
            for j in range(i,length):
                data[i], data[j] = data[j], data[i]
                permute(data, i+1, length)
                data[i], data[j] = data[j], data[i]

    permutations = []
    permute(list(range(n)), 0, n)  # Adjusted range
    return permutations


def all_matrix_permutations(matrix):
    """
    This function returns all possible matrices with permuted columns.
    It takes as input a matrix.
    If the matrix is empty or the first row is empty, it returns a list containing an empty list.
    Otherwise, it generates all possible matrices with permuted columns and returns these matrices.
    """
    if not matrix or not matrix[0]:
        return [[]]

    n = len(matrix[0])  # number of columns
    permutations = all_permutations(n)  # get all permutations of columns
    permuted_matrices = [matrix_column_permutation(matrix, p) for p in permutations]  # generate all permuted matrices
    return permuted_matrices


def largest_submatrix(matrix):
    """
    This function returns the area of the largest sub-matrix with all ones.
    It takes as input a binary matrix.
    If the matrix is empty or the first row is empty, it returns 0.
    Otherwise, it generates all possible matrices with permuted columns.
    Then, it evaluates the area of the largest sub-matrix for each permuted matrix and returns the maximum area found.
    """
    if not matrix or not matrix[0]:
        return 0

    permuted_matrices = all_matrix_permutations(matrix)

    max_area = 0
    for m in permuted_matrices:
        area = eval_matrix(m)
        if area > max_area:
            max_area = area

    return max_area