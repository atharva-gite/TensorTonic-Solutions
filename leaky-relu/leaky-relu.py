import numpy as np

def leaky_relu(x, alpha=0.01):

    answer_arr=[]
    for num in x:
        if num>=0:
            answer_arr.append(num)
        else:
            answer_arr.append(alpha*num)
    return np.array(answer_arr)