import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    C = np.asarray(C)

    row_arr = np.sum(C, axis=1)
    col_arr = np.sum(C, axis=0)
    total = np.sum(C)

    # Convert row totals to column vector
    row_arr = row_arr.reshape(-1, 1)

    # Expected frequencies
    exp_arr = row_arr * col_arr / total

    # Chi-square contributions
    chi = (C - exp_arr) ** 2 / exp_arr

    return (np.sum(chi), exp_arr)