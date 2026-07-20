import numpy as np

def sample_var_std(x):
    s_2=0
    xmean=np.mean(x)
    for num in x:
        s_2+=(xmean-num)**2
    n=len(x)
    return s_2/(n-1),np.sqrt(s_2/(n-1))