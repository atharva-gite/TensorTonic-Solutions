import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows=len(A)
    cols=len(A[0])
    AT = [[0] * rows for _ in range(cols)]
    for j in range(rows):
        for i in range(cols):
            AT[i][j]=A[j][i]

    return np.array(AT)
