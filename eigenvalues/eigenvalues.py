import numpy as np

def calculate_eigenvalues(matrix):
    if not isinstance(matrix, (list, tuple, np.ndarray)):
        return None

    rows = [np.asarray(row) for row in matrix]

    if len(rows) == 0:
        return None

    if not all(row.ndim == 1 for row in rows):
        return None

    if not all(len(row) == len(rows[0]) for row in rows):
        return None

    if len(rows) != len(rows[0]):
        return None

    matrix = np.array(rows)

    values = np.linalg.eigvals(matrix)

    return np.sort(values)