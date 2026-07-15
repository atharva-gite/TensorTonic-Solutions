import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    arr=np.array(x)
    result=1/(1+np.exp(-arr))
    return result