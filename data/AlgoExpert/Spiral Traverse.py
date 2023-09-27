def spiralTraverse(array):
    result = []
    spiral_fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result

def spiral_fill(array, beg_row, end_row, beg_col, end_col, result):
    if beg_row > end_row or beg_col > end_col:
        return

    for col in range(beg_col, end_col + 1):
        result.append(array[beg_row][col])

    for row in range(beg_row + 1, end_row + 1):
        result.append(array[row][end_col])

    for col in reversed(range(beg_col, end_col)):
        if beg_row == end_row:
            break
        result.append(array[end_row][col])

    for row in reversed(range(beg_row + 1, end_row)):
        if beg_col == end_col:
            break
        result.append(array[row][beg_col])

    spiral_fill(array, beg_row + 1, end_row - 1, beg_col + 1, end_col -1, result)
    
