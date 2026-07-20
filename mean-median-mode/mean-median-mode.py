import numpy as np
from collections import Counter

def calc_mean(x):
    sum=0
    for num in x:
        sum+=num
    return sum/len(x)
def calc_median(x):
    x=sorted(x)
    length=len(x)
    if length%2==1:
        return x[length//2]
    else:
        return (x[length//2]+x[length//2-1])/2
def calc_mode(x):
    freq={}
    for num in x:
        freq[num]=freq.get(num,0)+1
    max_freq=max(freq.values())
    mode=[key for key, value in freq.items() if value == max_freq]
    return min(mode)
def mean_median_mode(x):
    return calc_mean(x),calc_median(x),calc_mode(x)