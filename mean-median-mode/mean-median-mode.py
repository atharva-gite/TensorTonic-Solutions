import numpy as np
from collections import Counter

def mean_median_mode(x):
    counts=Counter(x)
    max_freq=max(counts.values())
    mode=min(num for num, freq in counts.items() if freq == max_freq)
    return np.mean(x),np.median(x),mode