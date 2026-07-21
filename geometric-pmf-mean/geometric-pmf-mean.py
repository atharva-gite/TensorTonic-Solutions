import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k=np.array(k)
    r=(1-p)**(k-1)*p
    return (r,1/p)