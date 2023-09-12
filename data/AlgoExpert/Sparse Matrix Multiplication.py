def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]

    sparse_a = get_sparse(matrix_a)
    sparse_b = get_sparse(matrix_b)

    result = [[0 for i in range(len(matrix_b[0]))] for j in range(len(matrix_a)) ]

    for i, k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b.keys():
                result[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]
    return result


def get_sparse(matrix):
    non_zero = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                non_zero[(i, j)] = matrix[i][j]
    return non_zero
