import numpy as np

def expected_value_discrete(x, p):
    if len(x) != len(p):
        raise ValueError("x and p must have the same length")

    if not np.isclose(sum(p), 1.0):
        raise ValueError("exception: probabilities must sum to 1")

    E_X = 0
    for i in range(len(x)):
        E_X += x[i] * p[i]

    return E_X
