import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a=np.array(a)
    b=np.array(b)
    numerator=a*b
    numsum=numerator.sum()
    den_a=a**2
    den_a=den_a.sum()
    den_b=b**2
    den_b=den_b.sum()
    if den_a==0 or den_b==0:
        return 0
    return numsum/np.sqrt(den_a*den_b)