import numpy as np

def swish(x):
    return ((x*np.exp(x))/(1+np.exp(x)))