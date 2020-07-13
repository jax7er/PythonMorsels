def add(*ms):
    ''' Element-wise add of list-of-lists (2D matricies) '''

    col_counts = {len(m) for m in ms}
    row_counts = {len(m_col) for m in ms for m_col in m}
    if len(col_counts) != 1 or len(row_counts) != 1:
        raise ValueError("Given matrices are not the same size.")

    result = []

    for m_cols in zip(*ms):
        sum_col = []

        for m_vals in zip(*m_cols):
            sum_col.append(sum(m_vals))

        result.append(sum_col)
    
    return result


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(add(matrix1, matrix2))
# [[3, -3], [-3, 3]]

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2))
# [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
print(add(matrix1, matrix2, matrix3))
# [[8, 8], [7, 7]]

print(add([[1, 9], [7, 3]], [[1, 2], [3]]))
